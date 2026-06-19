"""
Collaptics predictions — assertion-based tests (reproduce the whitepaper numbers).

Run any of:
    python3 test_predictions.py          # plain: prints + asserts, exits non-zero on fail
    python3 -m pytest test_predictions.py -v   # if pytest installed

Each test states the FORMULA it checks, so you can verify the number by hand,
not just trust the print-out. Deterministic seeds → same numbers every run.
"""

import numpy as np
from collapse_sim import (langevin_samples, _double_well, _laplace_pleft,
                          _count_crossings, mfpt)


# ---------------------------------------------------------------------------
# P1 — Inverse-square sharpening.   V = 0.5*lam*x^2  =>  sigma^2 = D/(Omega^2 lam)
#      => log(sigma^2) = const - 2*log(Omega).  We assert the fitted slope ≈ -2.
# ---------------------------------------------------------------------------
def test_p1_inverse_square_slope():
    lam, D = 2.0, 0.5
    omegas = np.array([0.6, 0.9, 1.3, 1.8, 2.6, 3.6, 5.0])
    gradV = lambda x: lam * x
    var = np.array([np.var(langevin_samples(gradV, Om, D,
                    rng=np.random.default_rng(100 + i)))
                    for i, Om in enumerate(omegas)])
    slope = np.polyfit(np.log(omegas), np.log(var), 1)[0]
    print(f"P1 slope = {slope:+.3f} (expect -2.000)")
    assert abs(slope + 2.0) < 0.06, f"slope {slope} not ~ -2"
    # also check absolute values match closed form within 6%
    theory = D / (omegas**2 * lam)
    rel = np.abs(var - theory) / theory
    assert rel.max() < 0.06, f"variance off theory by {rel.max():.1%}"


# ---------------------------------------------------------------------------
# P2 — Coherence == temperature.   beta = Omega^2/D.  Hold Omega^2/D fixed,
#      vary (Omega, D); the stationary variance must be invariant.
# ---------------------------------------------------------------------------
def test_p2_coherence_equals_temperature():
    lam = 2.0
    gradV = lambda x: lam * x
    pairs = [(1.0, 0.5), (1.4142, 1.0), (2.0, 2.0), (0.7071, 0.25)]  # Omega^2/D = 2
    var = [np.var(langevin_samples(gradV, Om, D, rng=np.random.default_rng(200 + i)))
           for i, (Om, D) in enumerate(pairs)]
    spread = np.std(var) / np.mean(var)
    print(f"P2 relative spread = {spread*100:.2f}% (expect <5%)")
    assert spread < 0.05, f"spread {spread:.3f} too large; Omega^2/D not a state variable"


# ---------------------------------------------------------------------------
# P3 — Cramer-Rao precision ceiling.  Var(x_hat) >= 1/Sigma = 1/(I*Omega^2).
#      Verify Sigma=1/sigma^2 equals I*Omega^2, the mean estimator achieves the
#      bound, and a median estimator cannot beat it (no estimator can).
# ---------------------------------------------------------------------------
def test_p3_cramer_rao_ceiling():
    lam, D, Omega = 2.0, 0.5, 1.5
    gradV = lambda x: lam * x
    s = langevin_samples(gradV, Omega, D, n_walkers=10000,
                         rng=np.random.default_rng(300)).ravel()
    Sigma = 1.0 / np.var(s)
    Sigma_theory = (lam / D) * Omega**2          # I * Omega^2
    M = 50
    g = s[: (len(s)//M)*M].reshape(-1, M)
    var_mean = np.var(g.mean(axis=1))
    var_median = np.var(np.median(g, axis=1))
    crb = 1.0 / (M * Sigma)
    print(f"P3 Sigma sim={Sigma:.3f} theory={Sigma_theory:.3f} "
          f"CRB={crb:.5f} mean={var_mean:.5f} median={var_median:.5f}")
    assert abs(Sigma - Sigma_theory)/Sigma_theory < 0.05, "Sigma != I*Omega^2"
    assert var_mean >= crb*0.9, "estimator beats Cramer-Rao bound (impossible)"
    assert abs(var_mean - crb)/crb < 0.15, "mean estimator should be efficient"
    assert var_median > crb*1.2, "inefficient estimator should be strictly worse"


# ---------------------------------------------------------------------------
# P5a — Basin-pull in the ERGODIC regime.  Landing prob follows Laplace
#       Gamma_k = exp(-beta V_k)/sqrt(curvature_k)  (depth x width).
#       Assert the simulated split matches Laplace AND the wide-shallow well wins.
# ---------------------------------------------------------------------------
def test_p5a_basin_pull_ergodic():
    xL, xR, VL, VR, kL, kR = -1.2, 1.2, -0.5, -0.2, 3.0, 0.6
    D, Omega = 0.9, 1.0
    beta = Omega**2 / D
    gradV, in_left = _double_well(xL, xR, VL, VR, kL, kR)
    rng = np.random.default_rng(11)
    x = rng.uniform(-3, 3, size=(12000, 1))
    coeff, om2 = np.sqrt(2*D*1e-3), Omega**2
    probe, samples = [], []
    for t in range(40000):
        x = x - om2*gradV(x)*1e-3 + coeff*rng.standard_normal(x.shape)
        probe.append(bool(in_left(x[0, 0])))
        if t >= 20000 and (t-20000) % 5 == 0:
            samples.append(x.copy())
    s = np.concatenate(samples, 0)
    p_left = float(np.mean(in_left(s)))
    pL_theory, _, _ = _laplace_pleft(VL, VR, kL, kR, beta)
    crossings = _count_crossings(np.array(probe))
    print(f"P5a P(left) sim={p_left:.3f} theory={pL_theory:.3f} crossings={crossings}")
    assert crossings > 20, "not ergodic — raise D or lower barrier"
    assert abs(p_left - pL_theory) < 0.06, "basin-pull split off Laplace"
    assert p_left < 0.5, "wide-shallow well should win (width beats depth)"


# ---------------------------------------------------------------------------
# P5b — Kinetic trapping (Pillar 3).  High barrier => field cannot equilibrate;
#       it stays trapped and the population does NOT match the Laplace split.
#       Assert ~0 crossings and a clear deviation from equilibrium.
# ---------------------------------------------------------------------------
def test_p5b_kinetic_trapping():
    xL, xR, VL, VR, kL, kR = -2.0, 2.0, -1.0, -0.4, 8.0, 0.8
    D, Omega = 0.7, 1.0
    beta = Omega**2 / D
    gradV, in_left = _double_well(xL, xR, VL, VR, kL, kR)
    rng = np.random.default_rng(7)
    x = np.zeros((8000, 1))
    coeff, om2 = np.sqrt(2*D*1e-3), Omega**2
    probe, samples = [], []
    for t in range(12000):
        x = x - om2*gradV(x)*1e-3 + coeff*rng.standard_normal(x.shape)
        probe.append(bool(in_left(x[0, 0])))
        if t >= 6000 and (t-6000) % 5 == 0:
            samples.append(x.copy())
    s = np.concatenate(samples, 0)
    p_left = float(np.mean(in_left(s)))
    pL_theory, _, _ = _laplace_pleft(VL, VR, kL, kR, beta)
    crossings = _count_crossings(np.array(probe))
    print(f"P5b P(left) sim={p_left:.3f} equilibrium={pL_theory:.3f} crossings={crossings}")
    assert crossings < 5, "expected kinetic trapping, but barrier was crossed"
    assert abs(p_left - pL_theory) > 0.2, "expected deviation from equilibrium"


# ---------------------------------------------------------------------------
# P6 — Arrhenius time-to-solution.  tau ~ exp(beta*dV).  Double well V=H(x^2-1)^2,
#      barrier dV=H. Vary beta; ln(tau) vs beta*dV must be linear with slope ~ 1.
# ---------------------------------------------------------------------------
def test_p6_arrhenius_slope():
    H, Omega = 0.8, 1.0
    gradV = lambda x: 4*H*x*(x**2 - 1)
    Ds = [0.40, 0.32, 0.26, 0.22]
    betas = np.array([Omega**2/D for D in Ds])
    out = [mfpt(gradV, Omega, D, n=2000, maxstep=260000,
                rng=np.random.default_rng(400+i)) for i, D in enumerate(Ds)]
    taus = np.array([t for t, _ in out]); fracs = [f for _, f in out]
    slope = np.polyfit(betas*H, np.log(taus), 1)[0]
    print(f"P6 ln-tau vs beta*dV slope = {slope:.3f} (expect 1.0), min frac={min(fracs):.2f}")
    assert min(fracs) > 0.9, "walkers did not cross — raise maxstep"
    assert 0.8 < slope < 1.2, f"slope {slope} not ~ 1 (Arrhenius law broken)"


if __name__ == "__main__":
    tests = [test_p1_inverse_square_slope, test_p2_coherence_equals_temperature,
             test_p3_cramer_rao_ceiling, test_p5a_basin_pull_ergodic,
             test_p5b_kinetic_trapping, test_p6_arrhenius_slope]
    failed = 0
    for t in tests:
        try:
            t()
            print(f"  PASS  {t.__name__}\n")
        except AssertionError as e:
            failed += 1
            print(f"  FAIL  {t.__name__}: {e}\n")
    print("=" * 50)
    print(f"{len(tests)-failed}/{len(tests)} predictions confirmed")
    raise SystemExit(1 if failed else 0)
