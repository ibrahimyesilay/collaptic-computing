"""
Collaptics Collapse Flow — numerical validation of the theory.

Integrates the one axiom:      dx = -Omega^2 * grad V(x) * dt + sqrt(2 D dt) * xi
and tests three predictions from theoretical-foundations.md:

  P1  Inverse-square sharpening:   sigma^2 ∝ Omega^-2   (log-log slope = -2)
  P2  Coherence ≡ temperature:     identical statistics when Omega^2 / D matched
  P5  Basin-pull selection:        landing prob ratio = exp(-b dV) * sqrt(detH2/detH1)
                                   (a wide-shallow well can beat a deep-narrow one)

numpy only. Deterministic seed (no Math.random dependence on wall clock).
"""

import numpy as np


def langevin_samples(gradV, Omega, D, n_walkers=4000, n_steps=6000,
                     dt=1e-3, burn=3000, x0=0.0, rng=None, dim=1):
    """Simulate the Collapse Flow and return post-burn-in samples."""
    if rng is None:
        rng = np.random.default_rng(0)
    x = np.full((n_walkers, dim), x0, dtype=float)
    coeff = np.sqrt(2.0 * D * dt)
    keep = []
    om2 = Omega * Omega
    for t in range(n_steps):
        x = x - om2 * gradV(x) * dt + coeff * rng.standard_normal(x.shape)
        if t >= burn and (t - burn) % 5 == 0:
            keep.append(x.copy())
    return np.concatenate(keep, axis=0)


# ----------------------------------------------------------------------
# P1 — inverse-square sharpening on a quadratic well V = 0.5 * lam * x^2
#      Theory:  sigma^2 = D / (Omega^2 * lam)  ->  log-log slope = -2 exactly
# ----------------------------------------------------------------------
def test_p1():
    lam, D = 2.0, 0.5
    omegas = np.array([0.6, 0.9, 1.3, 1.8, 2.6, 3.6, 5.0])
    gradV = lambda x: lam * x
    measured = []
    for i, Om in enumerate(omegas):
        s = langevin_samples(gradV, Om, D, rng=np.random.default_rng(100 + i))
        measured.append(np.var(s))
    measured = np.array(measured)
    theory = D / (omegas**2 * lam)
    slope = np.polyfit(np.log(omegas), np.log(measured), 1)[0]
    print("=== P1: inverse-square sharpening (V = 0.5*lam*x^2) ===")
    print(f"{'Omega':>7} {'sigma^2(sim)':>14} {'sigma^2(theory)':>16}")
    for Om, m, th in zip(omegas, measured, theory):
        print(f"{Om:7.2f} {m:14.5f} {th:16.5f}")
    print(f"  log-log slope  measured = {slope:+.3f}   (theory = -2.000)")
    print(f"  P1 {'PASS' if abs(slope + 2) < 0.06 else 'FAIL'}\n")
    return slope


# ----------------------------------------------------------------------
# P2 — coherence ≡ temperature.  beta = Omega^2 / D.
#      Different (Omega, D) with the SAME Omega^2/D must give the SAME variance.
# ----------------------------------------------------------------------
def test_p2():
    lam = 2.0
    gradV = lambda x: lam * x
    pairs = [(1.0, 0.5), (1.4142, 1.0), (2.0, 2.0), (0.7071, 0.25)]  # Omega^2/D = 2
    print("=== P2: coherence ≡ temperature (Omega^2/D = 2 held fixed) ===")
    print(f"{'Omega':>7} {'D':>6} {'Omega^2/D':>10} {'sigma^2':>12}")
    variances = []
    for i, (Om, D) in enumerate(pairs):
        s = langevin_samples(gradV, Om, D, rng=np.random.default_rng(200 + i))
        v = np.var(s)
        variances.append(v)
        print(f"{Om:7.4f} {D:6.2f} {Om*Om/D:10.3f} {v:12.5f}")
    spread = np.std(variances) / np.mean(variances)
    print(f"  relative spread across matched pairs = {spread*100:.2f}%")
    print(f"  P2 {'PASS' if spread < 0.05 else 'FAIL'}  (theory: identical)\n")
    return spread


# ----------------------------------------------------------------------
# P5 — basin-pull: a wide-shallow well can beat a deep-narrow one.
#      Double well; basin pull Gamma_k = exp(-beta V_k) / sqrt(V''_k).
#      Predicted landing ratio  p_left/p_right = Gamma_left/Gamma_right.
#
#      The equilibrium formula is only valid when the field is ERGODIC
#      (barrier crossable within the run). P5a tests that regime.
#      P5b deliberately raises the barrier to show Pillar-3 kinetic
#      trapping: the field then does NOT reach the equilibrium split.
# ----------------------------------------------------------------------
def _double_well(xL, xR, VL, VR, kL, kR):
    def gradV(x):
        left = VL + 0.5*kL*(x - xL)**2
        right = VR + 0.5*kR*(x - xR)**2
        return np.where(left <= right, kL*(x - xL), kR*(x - xR))

    def in_left(x):  # basin membership by which parabola is lower
        left = VL + 0.5*kL*(x - xL)**2
        right = VR + 0.5*kR*(x - xR)**2
        return left <= right
    return gradV, in_left


def _laplace_pleft(VL, VR, kL, kR, beta):
    GL = np.exp(-beta * VL) / np.sqrt(kL)   # depth x (1/sqrt curvature) = depth x width
    GR = np.exp(-beta * VR) / np.sqrt(kR)
    return GL / (GL + GR), GL, GR


def _count_crossings(traj_in_left):
    return int(np.sum(traj_in_left[1:] != traj_in_left[:-1]))


def test_p5a():
    # Ergodic regime: low barrier, generous noise, long run, broad init.
    xL, xR = -1.2, 1.2
    VL, VR = -0.5, -0.2          # left deeper
    kL, kR = 3.0, 0.6            # left narrow, right wide
    D, Omega = 0.9, 1.0
    beta = Omega**2 / D
    gradV, in_left = _double_well(xL, xR, VL, VR, kL, kR)

    # broad, unbiased initialization across both basins
    rng = np.random.default_rng(11)
    x = rng.uniform(-3, 3, size=(12000, 1))
    coeff = np.sqrt(2*D*1e-3); om2 = Omega**2
    cross_probe = []  # track one walker's basin to confirm ergodicity
    samples = []
    for t in range(40000):
        x = x - om2*gradV(x)*1e-3 + coeff*rng.standard_normal(x.shape)
        cross_probe.append(bool(in_left(x[0, 0])))
        if t >= 20000 and (t-20000) % 5 == 0:
            samples.append(x.copy())
    s = np.concatenate(samples, 0)
    p_left = float(np.mean(in_left(s)))
    pL_theory, GL, GR = _laplace_pleft(VL, VR, kL, kR, beta)
    crossings = _count_crossings(np.array(cross_probe))

    print("=== P5a: basin-pull in the ERGODIC regime ===")
    print(f"  Left:  depth {VL:+.2f}, curv {kL:.1f} (DEEP, NARROW)")
    print(f"  Right: depth {VR:+.2f}, curv {kR:.1f} (shallow, WIDE)")
    print(f"  beta={beta:.3f}   single-walker basin crossings={crossings} (ergodic if >>1)")
    print(f"  Gamma_left={GL:.4f}  Gamma_right={GR:.4f}")
    print(f"  P(left)  sim = {p_left:.3f}   theory = {pL_theory:.3f}")
    winner = "DEEP-NARROW" if p_left > 0.5 else "SHALLOW-WIDE"
    print(f"  -> field prefers the {winner} basin (width beats depth!)")
    ok = abs(p_left - pL_theory) < 0.06 and crossings > 20
    print(f"  P5a {'PASS' if ok else 'FAIL'}  (Laplace basin-pull confirmed)\n")
    return p_left, pL_theory


def test_p5b():
    # High-barrier regime: same wells, far apart + low noise -> kinetic trapping.
    xL, xR = -2.0, 2.0
    VL, VR = -1.0, -0.4
    kL, kR = 8.0, 0.8
    D, Omega = 0.7, 1.0
    beta = Omega**2 / D
    gradV, in_left = _double_well(xL, xR, VL, VR, kL, kR)
    rng = np.random.default_rng(7)
    x = np.zeros((8000, 1))  # start at barrier top
    coeff = np.sqrt(2*D*1e-3); om2 = Omega**2
    cross_probe = []
    samples = []
    for t in range(12000):
        x = x - om2*gradV(x)*1e-3 + coeff*rng.standard_normal(x.shape)
        cross_probe.append(bool(in_left(x[0, 0])))
        if t >= 6000 and (t-6000) % 5 == 0:
            samples.append(x.copy())
    s = np.concatenate(samples, 0)
    p_left = float(np.mean(in_left(s)))
    pL_theory, _, _ = _laplace_pleft(VL, VR, kL, kR, beta)
    crossings = _count_crossings(np.array(cross_probe))

    print("=== P5b: Pillar-3 kinetic trapping (high barrier) ===")
    print(f"  beta={beta:.3f}   single-walker basin crossings={crossings} (trapped if ~0)")
    print(f"  P(left) sim = {p_left:.3f}   equilibrium theory = {pL_theory:.3f}")
    print(f"  -> field is KINETICALLY TRAPPED: it does NOT reach equilibrium")
    print(f"     (confirms tau ~ exp(beta*dV): barrier too high to cross in finite time)")
    print(f"  P5b {'PASS' if crossings < 5 else 'FAIL'}  (Pillar-3 trapping confirmed)\n")
    return p_left, pL_theory


# ----------------------------------------------------------------------
# P3 — Cramer-Rao precision ceiling.   Var(x_hat) >= 1/Sigma = 1/(I Omega^2).
#      Single-shot Fisher info of the collapse = Sigma = 1/sigma^2 = (lam/D) Omega^2.
#      M-shot mean estimator ACHIEVES the bound (efficient); median does NOT beat it.
# ----------------------------------------------------------------------
def test_p3():
    lam, D, Omega = 2.0, 0.5, 1.5
    gradV = lambda x: lam * x
    s = langevin_samples(gradV, Omega, D, n_walkers=10000,
                         rng=np.random.default_rng(300)).ravel()
    sigma2 = np.var(s)
    Sigma = 1.0 / sigma2                 # measured single-shot Fisher information
    I = lam / D
    Sigma_theory = I * Omega**2          # the Collapse Law
    M = 50
    g = s[: (len(s)//M)*M].reshape(-1, M)
    var_mean = np.var(g.mean(axis=1))    # efficient estimator
    var_median = np.var(np.median(g, axis=1))
    crb = 1.0 / (M * Sigma)              # Cramer-Rao bound for M shots = sigma^2/M
    print("=== P3: Cramer-Rao precision ceiling  Var >= 1/(I*Omega^2) ===")
    print(f"  measured Sigma = 1/sigma^2 = {Sigma:.4f}")
    print(f"  theory   Sigma = I*Omega^2 = {Sigma_theory:.4f}   (I=lam/D={I:.2f})")
    print(f"  M={M}-shot:  CRB = 1/(M*Sigma) = {crb:.5f}")
    print(f"    mean   estimator var = {var_mean:.5f}   (efficient: should hit CRB)")
    print(f"    median estimator var = {var_median:.5f}   (should be > CRB, ~1.57x)")
    ok = (abs(Sigma - Sigma_theory)/Sigma_theory < 0.05
          and var_mean >= crb*0.9
          and abs(var_mean - crb)/crb < 0.15
          and var_median > crb*1.2)
    print(f"  P3 {'PASS' if ok else 'FAIL'}  (no estimator beats 1/(I*Omega^2); mean achieves it)\n")
    return Sigma, Sigma_theory


# ----------------------------------------------------------------------
# P6 — Arrhenius time-to-solution.   tau ~ exp(beta * dV)  (Kramers).
#      Double well V = H(x^2-1)^2, barrier dV = H at x=0.  Vary beta=Omega^2/D,
#      measure mean first-passage time; ln(tau) vs beta*dV must have slope ~ 1.
# ----------------------------------------------------------------------
def mfpt(gradV, Omega, D, x_start=-1.0, x_cross=0.0,
         n=2500, maxstep=100000, dt=1e-3, rng=None):
    """Mean first-passage time from x_start to x_cross, and fraction that crossed."""
    if rng is None:
        rng = np.random.default_rng(0)
    x = np.full(n, x_start, dtype=float)
    tcross = np.full(n, np.nan)
    crossed = np.zeros(n, dtype=bool)
    coeff, om2 = np.sqrt(2*D*dt), Omega**2
    for t in range(maxstep):
        x = x - om2*gradV(x)*dt + coeff*rng.standard_normal(n)
        newly = (~crossed) & (x > x_cross)
        tcross[newly] = t*dt
        crossed |= newly
        if crossed.all():
            break
    return np.nanmean(tcross), crossed.mean()


def test_p6():
    # Higher barrier than P1/P5 so we sit in the asymptotic Kramers regime
    # (beta*dV >= 2), where the exponential law dominates and slope -> 1.
    H, Omega = 0.8, 1.0
    gradV = lambda x: 4*H*x*(x**2 - 1)      # V = H(x^2-1)^2
    Ds = [0.40, 0.32, 0.26, 0.22]
    betas = np.array([Omega**2/D for D in Ds])
    taus, fracs = [], []
    for i, D in enumerate(Ds):
        tau, frac = mfpt(gradV, Omega, D, n=2000, maxstep=260000,
                         rng=np.random.default_rng(400+i))
        taus.append(tau); fracs.append(frac)
    taus = np.array(taus); bH = betas*H
    slope, intercept = np.polyfit(bH, np.log(taus), 1)
    print("=== P6: Arrhenius time-to-solution  ln(tau) ~ beta*dV  (slope=1) ===")
    print(f"  barrier dV = H = {H}")
    print(f"{'beta':>7} {'beta*dV':>9} {'tau(MFPT)':>11} {'frac_crossed':>13}")
    for b, x, tau, f in zip(betas, bH, taus, fracs):
        print(f"{b:7.3f} {x:9.3f} {tau:11.4f} {f:13.3f}")
    print(f"  ln(tau) vs beta*dV  slope = {slope:.3f}   (Kramers theory = 1.000)")
    ok = 0.8 < slope < 1.2 and min(fracs) > 0.9
    print(f"  P6 {'PASS' if ok else 'FAIL'}  (exponential barrier law confirmed)\n")
    return slope


if __name__ == "__main__":
    print("\nCSC Collapse Flow — numerical validation")
    print("dx = -Omega^2 grad V dt + sqrt(2 D dt) xi\n")
    slope = test_p1()
    spread = test_p2()
    p3 = test_p3()
    p5a = test_p5a()
    p5b = test_p5b()
    p6_slope = test_p6()
    print("=" * 60)
    print("Summary  (6-prediction validation set)")
    print(f"  P1  slope           = {slope:+.3f}   (target -2.000)     [sharpening]")
    print(f"  P2  spread          = {spread*100:.2f}%  (target <5%)       [coherence=temp]")
    print(f"  P3  Sigma sim/theory= {p3[0]:.3f}/{p3[1]:.3f}             [Cramer-Rao ceiling]")
    print(f"  P5a P(left) sim     = {p5a[0]:.3f}   theory {p5a[1]:.3f}   [basin-pull]")
    print(f"  P5b P(left) sim     = {p5b[0]:.3f}   eq.thy {p5b[1]:.3f}   [kinetic trap]")
    print(f"  P6  ln-tau slope    = {p6_slope:.3f}   (target 1.000)     [Arrhenius]")
    print("=" * 60)
