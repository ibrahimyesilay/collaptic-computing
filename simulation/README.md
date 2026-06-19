# How to test the Collaptics numbers yourself

Everything in the whitepaper's "validation" section is reproducible in pure Python
(numpy only — no scipy, no GPU). This guide tells you **what each number is, the
formula it must match, how to run it, and how to check it by hand.**

## Setup

```bash
cd collaptic-computing/simulation
python3 -c "import numpy"        # the only dependency
```

## Two ways to run

```bash
# 1) See the numbers, with a printed PASS/FAIL table:
python3 collapse_sim.py

# 2) Run them as real tests (asserts; exits non-zero if any prediction fails):
python3 test_predictions.py
#   or, if you have pytest:
python3 -m pytest test_predictions.py -v
```

Both use **fixed random seeds**, so you get the *same* numbers every run — that is
the point: the claims are deterministic and checkable, not cherry-picked.

## What is actually being simulated

A single line — the Collaptics axiom (the Collapse Flow), integrated with Euler–Maruyama:

```python
x = x - Omega**2 * gradV(x) * dt + sqrt(2*D*dt) * randn()
```

That's it. Everything else is measuring the statistics of where `x` ends up.

## The four numbers and how to verify each

### P1 — slope = −1.989  (claim: σ² ∝ Ω⁻²)
- **Setup:** quadratic well `V = ½·λ·x²`, so `gradV = λx`.
- **Closed form (statistical mechanics):** the stationary distribution is Gaussian
  with `σ² = D / (Ω²·λ)`. Take logs → `log σ² = const − 2·log Ω`. **Slope must be −2.**
- **How to check by hand:** the printed table gives `sigma^2(sim)` next to
  `sigma^2(theory) = D/(Ω²λ)`. They match column-by-column to ~3 %. The fit of
  `log σ²` vs `log Ω` gives **−1.989**.
- **Falsifies the Collapse Law if:** slope ≠ −2. This is prediction P1 in the paper.

### P2 — spread = 0.20 %  (claim: Ω²/D is an inverse temperature)
- **Setup:** same well, four different `(Ω, D)` pairs all chosen so `Ω²/D = 2`.
- **Closed form:** `σ² = D/(Ω²λ) = 1/(λ·β)` with `β = Ω²/D`. If `β` is fixed,
  `σ²` must be **identical** regardless of how you split it into Ω and D.
- **Result:** all four variances ≈ 0.250 (spread 0.20 %). Coherence (ρ, via Ω) and
  noise (D) are interchangeable — raising coherence == lowering temperature.

### P3 — Σ = 9.033 vs 9.000  (claim: Cramér–Rao precision ceiling Var ≥ 1/(I·Ω²))
- **Setup:** quadratic well; measure the collapse width `σ²`, so the single-shot
  Fisher information is `Σ = 1/σ²`.
- **Closed form:** `Σ` must equal `I·Ω²` with `I = λ/D`. Then the Cramér–Rao bound
  on estimating the answer from `M` independent collapses is `CRB = 1/(M·Σ)`.
- **The test does three things:** (1) checks `1/σ² ≈ I·Ω²` (9.033 vs 9.000);
  (2) shows the **mean** estimator *achieves* the bound (`var_mean ≈ CRB`);
  (3) shows the **median** estimator is *worse* (`≈1.57×` CRB) — i.e. no estimator
  beats `1/(I·Ω²)`, and the efficient one saturates it. This is `Σ` as a hard
  physical accuracy limit, not a metaphor.

### P5a — P(left) = 0.394 vs theory 0.384  (claim: width can beat depth)
- **Setup:** an asymmetric double well. Left = **deep & narrow**
  (depth −0.5, curvature 3.0). Right = **shallow & wide** (depth −0.2, curvature 0.6).
- **Closed form (Laplace / "informational gravity"):** each basin's pull is
  `Γ_k = exp(−β·V_k) / sqrt(curvature_k)` — depth **times width**. Landing
  probability `P(left) = Γ_L/(Γ_L+Γ_R)`.
- **Non-obvious prediction:** despite being *shallower*, the wide right well wins,
  because its larger phase-space volume out-pulls the deep narrow one. Sim 0.394 vs
  Laplace 0.384 — confirmed to ~1 %.
- **Ergodicity guard:** the test also prints `crossings=177` for a single walker —
  proof the field actually explores both basins (so the equilibrium formula applies).

### P5b — P(left) = 0.103 vs equilibrium 0.427  (claim: honest boundary)
- **Setup:** wells pushed far apart with low noise → a **high barrier**.
- **What happens:** `crossings = 0`. The field cannot cross the barrier in finite
  time, so it gets **kinetically trapped** and does **not** reach the equilibrium
  split — exactly Pillar 3's `τ ∝ exp(β·ΔV)`.
- **Why this matters:** it is the simulator *drawing Collaptics' own limit*. The same code
  that confirms the law (P5a) also shows where the law's equilibrium prediction fails
  (P5b). Collaptics is an energy/throughput win on *crossable* landscapes — **not** a free
  solver of glassy / NP-hard / gradient-free problems.

### P6 — slope = 0.991  (claim: time-to-solution τ ∝ exp(β·ΔV), Arrhenius)
- **Setup:** a quartic double well `V = H(x²−1)²`, barrier height `ΔV = H` at x=0,
  minima at x=±1. Walkers start in the left well; we measure the **mean
  first-passage time** (MFPT) to cross to the right.
- **Closed form (Kramers):** `τ = prefactor · exp(β·ΔV)`, so `ln τ = β·ΔV + const`
  → **slope of `ln τ` vs `β·ΔV` must be 1.**
- **How to check:** vary `β = Ω²/D` over four values, read off the printed MFPT,
  fit `ln τ` against `β·ΔV`. Slope = **0.991** (deep in the Kramers regime,
  β·ΔV ≥ 2; at lower barriers a finite-barrier correction raises it toward ~1.2).
- **Why it matters:** this is the *quantitative* statement of Collaptics' complexity
  boundary — hard (high-barrier) problems cost exponentially more time. The
  energy win is real only where `ΔV` is small.

## Change the numbers and watch the theory respond

To probe the results, vary the parameters and confirm the theory still holds:

```python
# In collapse_sim.py test_p1(): widen the Omega sweep — slope stays -2.
omegas = np.array([0.4, 0.7, 1.0, 2.0, 4.0, 8.0])

# In test_p5a(): lower the right-well curvature kR (make it even wider).
# Prediction: P(left) drops further — the wider well pulls even harder.

# In test_p5b(): raise D (more noise) until crossings > 20.
# Prediction: it becomes ergodic and P(left) jumps toward the equilibrium 0.427.
```

If any of these stops matching the closed-form formula, the theory is wrong —
which is exactly the falsifiability the whitepaper claims.

## Files

| File | Purpose |
|---|---|
| `collapse_sim.py` | the simulator + a printed PASS/FAIL report |
| `test_predictions.py` | assertion-based tests (the formulas, enforced) |
| `RESULTS.md` | the reference numbers from a clean run |
| `README.md` | this guide |
