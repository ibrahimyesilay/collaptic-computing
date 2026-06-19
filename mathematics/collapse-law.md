# The Collapse Law — Derivation of Σ = I·Ω²
*Mathematical core of Collaptic Computing*

This document derives the Collaptics constitutive law

```
Σ = I·Ω² ,        Ω = ρ·ω
```

from a single equation of motion, and ends with falsifiable predictions. Nothing here invokes new physics — every step rests on established stochastic dynamics (Langevin / Fokker–Planck), Hopfield–Ising energy landscapes, and Fisher information. Collaptics' novelty is the *identification* of the substrate's coherent resonance `Ω` with the mobility of an informational gradient flow, not a new force of nature.

---

## 0. Objects

| Symbol | Object | Established analogue |
|---|---|---|
| `x ∈ ℝⁿ` | system configuration (a candidate solution) | state vector |
| `P(x,t)` | the **informational field** — probability density over configurations (the Collapton cloud) | probability density |
| `V(x)` | **informational potential** — the problem as a landscape; minima = good solutions | Hopfield/Ising energy `E = −½ Σ wᵢⱼ sᵢsⱼ` |
| `ρ` | confidence density of the substrate (phase-locking / coherence) | coherence |
| `ω` | resonance signature of the substrate (mode frequency) | oscillator / photon frequency |
| `Ω = ρω` | **coherent resonance** — the unified conversion constant | coherent field amplitude (laser) |
| `D = η₀` | exploration temperature (controlled noise power) | thermal noise / annealing temp |

A **Collapse Singularity** is a dominant local minimum `x*` of `V`: the deepest attractor the field can reach.

---

## 1. Axiom — the Collapse Flow

Collaptics postulates exactly one law of motion. The field's representative state evolves by overdamped stochastic gradient descent, where **the mobility is the squared coherent resonance of the substrate**:

```
 (1)     dx/dt = −Ω²·∇V(x) + √(2D)·ξ(t)
```

with white noise `⟨ξ(t)⟩ = 0`, `⟨ξ(t)·ξ(t′)⟩ = δ(t − t′)`.

This is the *only* assumption unique to Collaptics: that a more coherent, higher-frequency substrate (`Ω` large) pulls the field downhill faster. Everything below is a consequence.

> **Why `Ω²` and not `Ω`?** Power delivered by a driven resonant mode scales as (amplitude)², and coupling energy in Hopfield/Ising landscapes is quadratic in the coupling strength. The mobility a resonant substrate can impart on a gradient flow therefore scales as `Ω²`. This is the same quadratic that puts the `c²` in `E = mc²` — a conversion *rate squared*.

---

## 2. Field-level evolution (Fokker–Planck)

The ensemble of trajectories (1) is equivalent to the evolution of the informational field `P(x,t)` via the Smoluchowski / Fokker–Planck equation:

```
 (2)     ∂P/∂t = ∇·[ Ω²·(∇V)·P + D·∇P ]
```

Equation (2) is the **field law of Collaptics**: the Collapton cloud drifts toward minima (term `Ω²·∇V`) while diffusing (term `D·∇P`). "Collapse" is this `P` becoming concentrated.

---

## 3. The collapse — stationary distribution

Set `∂P/∂t = 0` and require zero probability flux. Equation (2) gives `Ω²·(∇V)·P* + D·∇P* = 0`, i.e. `∇ ln P* = −(Ω²/D)·∇V`, so

```
 (3)     P*(x) ∝ exp[ −(Ω²/D)·V(x) ]
```

This is the central result of the static theory:

**Coherent resonance acts as an inverse temperature.** The factor `β ≡ Ω²/D` plays the exact role of `1/(k_B·T)` in statistical mechanics. Raising the substrate's coherence `ρ` or frequency `ω` *cools* the informational field, sharpening it onto the deepest attractor. This is the precise meaning of "the machine converges instead of computing": at large `Ω`, `P*` is a near-delta at `x*`.

---

## 4. Geometry of the singularity

Expand `V` about the dominant minimum `x*` (the Collapse Singularity). Since `∇V(x*) = 0`,

```
 (4)     V(x) ≈ V(x*) + ½·(x − x*)ᵀ·H·(x − x*) ,      H = ∇²V(x*) ≻ 0
```

`H` is the **curvature of the attractor** — how steeply the well closes around the answer. Substituting (4) into (3), the collapsed field is Gaussian:

```
 (5)     P*(x) ≈ 𝒩( x* , (D/Ω²)·H⁻¹ )         ← covariance = (D/Ω²)·H⁻¹
```

The width of the answer along curvature mode `λ` (an eigenvalue of `H`) is

```
 (6)     σ² = D / (Ω²·λ)      ⟹      σ² ∝ 1/Ω²
```

The collapsed answer gets quadratically sharper as coherent resonance rises.

---

## 5. Definition of Σ and the Collapse Law

Define **Singularity strength** `Σ` as the *resolving power* of the collapse: the precision (inverse variance) with which the field pins down the answer. This is exactly the **Fisher information** the field carries about `x*` — the curvature of `ln P*`:

```
 (7)     Σ ≡ −∂²(ln P*)/∂x² = 1/σ² = (λ/D)·Ω²
```

Now identify the **information content of the field**, the part intrinsic to the *problem* (not the substrate):

```
         I := λ/D = (attractor curvature) / (exploration noise)
```

`I` is a genuine information quantity: curvature of a log-density *is* Fisher information, and dividing by noise power makes it the field's signal-to-noise — the bits the landscape can resolve. Substituting:

```
 (8)     Σ = I·Ω²        ∎
```

**Reading.** The resolving power of a collapse equals the field's latent information `I` (set by the problem's geometry and the noise budget) times the square of the substrate's coherent resonance `Ω = ρω` (set by the hardware). The problem contributes linearly; the *photonic-resonant collapse* contributes quadratically.

---

## 6. Corollaries (what the law buys you)

**6.1 — Precision bound (Cramér–Rao).** Any readout of the answer obeys

```
         Var(x̂) ≥ 1/Σ = 1/(I·Ω²)
```

So `Σ` is not a metaphor — it is a hard lower bound on achievable answer error. A Collaptics machine's accuracy ceiling is fixed by `I·Ω²`. This makes the **Collapse Throughput** metric in the whitepaper a measurable rate: `CT = dΣ/dt`.

**6.2 — Thermodynamic cost (Landauer).** Collapse lowers the field's entropy by `ΔH = ½·ln(Σ/Σ₀)` per mode; by Landauer this costs at least `k_B·T·ΔH` of energy. The answer is paid for in entropy reduction — Collaptics inherits a real thermodynamic floor, not free computation.

**6.3 — Why analog/photonic wins.** Doubling substrate coherence `Ω` → `4×` resolving power `Σ` at the *same* information `I` and *same* energy landscape. A digital machine must spend proportionally more operations to halve variance; a coherent substrate gets it from physics. This is the quantitative version of "memory = compute."

**6.4 — Recovery of search.** When `Ω → 0` (no coherence), `P*` flattens to uniform — pure random search. When `Ω → ∞` (perfect coherence, no noise), `P* → δ(x − x*)` — deterministic collapse. Collaptics interpolates between brute-force and oracle, with `Ω` as the dial.

---

## 7. Assumptions and limits

The derivation is valid only under the following conditions:

1. **Overdamped, Markovian dynamics** (eq. 1). Underdamped/inertial substrates need a second-order extension.
2. **Local result.** Eqs. (4)–(8) describe the *dominant* well. `Σ = I·Ω²` is the resolving power onto an attractor — it does **not** assert that attractor is the global optimum. Collaptics, like every annealing/Ising machine, can land in a local minimum. *This is the central limit of the method: Collaptics does not solve NP-hard problems for free.*
3. **Quadratic approximation** near `x*` (Gaussian collapse). Heavy-tailed or rugged wells deviate.
4. **Stationarity reached** — the field must be annealed long enough to equilibrate; finite-time collapse has a correction `∼ exp(−Ω²·λ·t)`.
5. **`V` must be physically realizable** as a landscape on the substrate. Problems with no exploitable gradient structure (e.g. cryptographic hashes, by design) have flat `V` → no attractor → Collaptics offers no advantage. *(This is why the hash-inversion example is dropped from the theory.)*

---

## 8. Falsifiable predictions

The framework makes the following testable predictions, several checkable on existing coherent Ising machines and optical annealers:

- **P1 — Inverse-square sharpening:** answer variance `σ² ∝ Ω⁻²`. Sweep substrate coherence/frequency, measure solution spread; slope on a log–log plot must be `−2`.
- **P2 — Coherence-as-temperature:** the solution distribution must follow `P* ∝ exp(−(Ω²/D)·V)` — i.e. raising coherence is interchangeable with lowering noise temperature. Measurable as identical solution statistics for matched `Ω²/D`.
- **P3 — Precision ceiling:** no readout beats `Var ≥ 1/(I·Ω²)`. A violation falsifies the law.
- **P4 — Quadratic energy advantage:** to reach a target precision, coherent-substrate energy cost scales `∝ 1/Ω²` versus a digital baseline's `∝` operation count.

If P1 (slope `≠ −2`) fails on real hardware, the relation `Σ = I·Ω²` is falsified.

---

## Summary

```
   dx/dt = −Ω²·∇V + √(2D)·ξ     →     P* ∝ exp(−(Ω²/D)·V)     →     Σ = I·Ω²
   └─ one axiom (Collapse Flow)         └────── collapse ──────┘        └ Collapse Law ┘
```

From one equation of motion, the constitutive relation follows in a few lines of stochastic calculus, together with a Cramér–Rao precision bound, a Landauer energy floor, and four falsifiable predictions. `Ω = ρω` retains both the photon (`ω`) and the collapse (`ρ`); the square follows from three independent areas of physics; and the limits (local minima, flat landscapes) are stated explicitly.
