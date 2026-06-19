# Collaptics — Theoretical Foundations
*Deep structure of Collaptic Computing: from one axiom to a unifying theory of physical computation*

This document hardens Collaptics from a single law (`Σ = I·Ω²`) into a full theoretical framework. The strategy throughout: **every Collaptics claim is anchored to an established theorem**, so the novelty is the *synthesis and the substrate identification* (`Ω = ρω` as the mobility of an informational flow), never new physics. Eleven pillars.

Notation carried from `collapse-law.md`: field `P(x,t)`, informational potential `V(x)`, coherent resonance `Ω = ρω`, exploration temperature `D`, inverse temperature `β ≡ Ω²/D`.

---

## Pillar 1 — Collapse is variational free-energy descent (the deep "why")

The Collapse Flow is not an arbitrary dynamics. Define the **informational free energy** of the field:

```
F[P] = ⟨V⟩_P − (1/β)·H[P] ,      H[P] = −∫ P·ln P dx
        └ fit the problem ┘   └ stay exploratory ┘
```

**Theorem (Jordan–Kinderlehrer–Otto, 1998).** The Fokker–Planck equation `∂_t P = ∇·[Ω²(∇V)P + D∇P]` is *exactly* the steepest-descent gradient flow of `F[P]` in the Wasserstein-2 geometry of probability measures, run at rate `Ω²`.

Consequences:
- **Collapse = free-energy minimization.** Collaptics does not "search"; it slides `F[P]` downhill in the space of probability fields. The unique minimizer is the Gibbs field `P* ∝ e^(−βV)` with `F_min = −(1/β)·ln Z`.
- This is the *same* objective as **variational Bayesian inference** and Friston's **free-energy principle / active inference**. Collaptics is therefore the physical-hardware realization of variational inference: the brain-style "minimize surprise" objective implemented as a resonant field.
- The two terms make the exploration–exploitation tradeoff a thermodynamic identity: `⟨V⟩` pulls to the answer, `H/β` resists premature collapse. Coherence `Ω` tilts the balance toward exploitation.

In summary, Collaptics computes by letting a probability field descend its own free-energy surface in the Wasserstein geometry.

---

## Pillar 2 — Informational Gravity, made into an equation

Section 6–7 of the original theory spoke of "informational gravity" and "attractor basins" metaphorically. Here it becomes a formula. With multiple singularities `{x_k*}`, Laplace's method gives the mass the field deposits in basin `k`:

```
p_k = Z_k / Z ,    Z_k = e^(−βV_k)·(2π/β)^(n/2)·(det H_k)^(−1/2) ,    H_k = ∇²V(x_k*)
```

Define the **basin pull** (the informational-gravity charge of singularity `k`):

```
Γ_k = e^(−βV_k) · (det H_k)^(−1/2)
       └ depth ┘   └ width / phase-space volume ┘
```

So a singularity attracts probability in proportion to **depth × basin volume** — a deep narrow well can *lose* to a shallower but much wider one (entropic advantage). This is the precise, non-metaphorical content of "answers pull the machine toward themselves," and it corrects a naive reading: the strongest attractor is not merely the deepest, it is the one with the largest `Γ_k`. Curvature `H_k` is the literal "spacetime bending" — the field follows `Γ`, just as mass follows the metric.

---

## Pillar 3 — Time-to-collapse and the complexity boundary

Resolving power `Σ = I·Ω²` is the *eventual* precision; it says nothing about *how long* collapse takes. That is governed by barrier crossing.

**Kramers escape rate** between basins over a barrier of height `ΔV`:

```
r ≈ (Ω²/2π)·√(λ_min·λ_barrier)·e^(−β·ΔV) ,      τ_collapse ∼ 1/r
```

Equivalently, the convergence time is set by the **spectral gap** `g` of the Fokker–Planck operator, `τ ∼ 1/g`, with `g ∼ Ω²·e^(−βΔV)` for the dominant barrier.

This yields the central limiting statement of the theory:

```
τ_collapse ∝ e^(β·ΔV_max)
```

**Where Collaptics helps and where it does not:**

| Landscape class | `ΔV_max` | Collaptics verdict |
|---|---|---|
| Convex / smooth (low barriers) | `O(1)` | **Exponential energy win** — physics descends in parallel, `τ` tiny |
| High-dimensional, mildly rugged | moderate | **Polynomial-ish advantage** over digital, energy-cheap |
| Glassy / NP-hard worst case | `O(n)` | **No free lunch** — `τ` exponential, same wall as simulated annealing |
| Flat (cryptographic hash) | no gradient | **Zero advantage** — `Γ_k` uniform, no attractor |

Collaptics' true claim is therefore narrow and defensible: *for landscapes whose barriers are low relative to their dimension, a coherent substrate reaches the Gibbs collapse at energy cost far below a digital machine simulating the same flow.* It is an **energy/throughput** advantage on a wide class of real problems, **not** a complexity-class miracle.

---

## Pillar 4 — The Embedding Theorem: Collaptics contains the known methods

Collaptics is positioned as the unifying continuous-time, hardware-native superset of probabilistic computation. This is made literal.

**Proposition (Embedding).** Each established method is a limit/corner of the Collapse Flow `dx = −Ω²∇V dt + √(2D) dW`:

| Limit / specialization | Recovered method |
|---|---|
| `D → 0` | deterministic **gradient descent** / steepest collapse |
| Euler–Maruyama discretization | **Unadjusted Langevin (MCMC)** |
| `V = −½ sᵀWs`, `x ∈ {±1}ⁿ` | **Hopfield network / Ising machine** |
| `β` ramped `0 → ∞` on a schedule | **Simulated / quantum annealing** |
| `V = −(1/β)·ln p_data`, learned score `∇ln p_t` | **Score-based diffusion generative models** |
| flow lifted to Fisher–Rao metric on an exponential family | **Natural-gradient / mean-field variational inference** |
| replicator form on the simplex | **Evolutionary / replicator dynamics** |

All of these solve the *same* free-energy descent (Pillar 1) with different encodings of `V`, different discretizations, and different substrates. Collaptics' contribution is to (a) run it in continuous time on a physical resonant medium, and (b) make `Ω = ρω` — the substrate's coherence — the tunable mobility that sets both speed (Pillar 3) and precision (`Σ = I·Ω²`). The embedding shows that Collaptics does not compete with these methods but describes their common physical limit.

---

## Pillar 5 — Substrate physics: deriving Ω = ρω and the decoherence floor

To stay defensible Collaptics commits to **classical wave coherence** (as in coherent optical / photonic Ising machines), not fragile qubit superposition. The substrate is a network of coupled resonant modes.

- **`ω`** — the angular frequency of the substrate's resonant modes. Energy stored/transferred per mode `∝ ω²` (oscillator), grounding the square.
- **`ρ`** — the **coherence** of the field: normalized off-diagonal correlation / fringe visibility, `ρ ∈ [0,1]`. `ρ = 1` is perfect phase-locking (a laser); `ρ = 0` is incoherent light (a lamp) — which computes nothing.
- **`Ω = ρω`** is then the *coherent* drive amplitude — frequency you can actually use, discounted by how phase-locked it stays. Incoherent high frequency (`ρ → 0`) gives `Ω → 0`: no collapse. This is why a resonant substrate must remain phase-coherent to compute; incoherent oscillation carries no usable drive.

**Decoherence floor.** Real coherence decays with time constant `T_φ`: `ρ(t) = ρ₀·e^(−t/T_φ)`. Collapse must finish before coherence dies, `τ_collapse < T_φ`. Combine with Kramers (Pillar 3), `τ ∝ e^(βΔV)`:

```
ΔV_max(usable) ≈ (1/β)·ln(T_φ/τ₀)
```

There is a *maximum barrier height a given substrate can cross before it decoheres*. This is the quantitative answer to the classic objection that analog noise is fatal: noise does not defeat Collaptics, it **bounds the problem hardness** a substrate of coherence `(ρ₀, T_φ)` can handle. Better materials (longer `T_φ`) directly buy harder problems — a clean engineering roadmap.

---

## Pillar 6 — Collapton algebra: the instruction set

For Collaptics to be programmable it needs operations, not just a unit. The Collapton `C = {μ, σ, ρ, φ, ω, τ}` supports a minimal, physically realizable operation set — the Collaptics "ISA":

| Operation | Action on the field | Physical realization |
|---|---|---|
| **Encode** `prob → V` | compile problem into the potential / couplings `J_ij` | set mode couplings, detunings |
| **Prime** `P₀ = Σ wᵢPᵢ` | initialize a broad superposition of tendencies | broadband / high-`D` injection |
| **Couple** `V = Σ Vᵢ + Σ J_ij` | build composite problems by interference | resonant coupling network |
| **Drive** `Ω(t)` schedule | anneal: lower `D` / raise `ρ` over time | pump power, gain schedule |
| **Collapse/Read** `x ∼ P*` | sample the converged field | homodyne / intensity readout |

Composition law: coupling Collaptons multiplies their fields and *adds* their log-potentials — so problem composition is **additive in `V`, multiplicative in `P`**, exactly the structure of a probabilistic graphical model. A Collaptics program is a coupling graph `{J_ij}` plus a drive schedule `Ω(t)`. This is the bridge from "physics" to "compiler."

---

## Pillar 7 — Robustness: how analog Collaptics suppresses device error

Binary won historically because it rejects noise; Collaptics must show it can too. Distinguish two noises:
- **`η(t)` / `D`** — *intended* exploration noise. Functional, not error (it sets `β`).
- **`δV`** — *device* error: fabrication variance, drift, crosstalk corrupting the potential.

Run `N` independent Collapton replicas of the same problem (an ensemble field). Device errors are independent zero-mean; the averaged potential has error `∝ σ_δV/√N`. Therefore the misplacement of the singularity shrinks as

```
‖x*_est − x*_true‖ ∝ 1/√N
```

Precision is **recoverable by redundancy** at energy cost `∝ N` — the analog counterpart of error correction. It is averaging, not fault-tolerant QEC, but for an optimizer/sampler it is sufficient and cheap, and it composes with Pillar 5: redundancy effectively lengthens usable `T_φ`.

---

## Pillar 8 — The thermodynamic triangle (the governing engineering law)

Three results bound the three things an engineer cares about:
- **Precision** (Cramér–Rao): `Var(x̂) ≥ 1/Σ = 1/(I·Ω²)`.
- **Speed** (Kramers): `τ ∝ e^(βΔV)`, and `β = Ω²/D`.
- **Energy** (Landauer + Jarzynski): collapse work `W ≥ k_B·T·ΔH = (k_B·T/2)·ln(Σ/Σ₀)` per mode; fluctuation theorem `⟨e^(−βW)⟩ = e^(−βΔF)` sets the dissipation.

These cannot be jointly maximized. Raising `Ω` improves precision *and* speed-per-barrier but *deepens* `β`, which **lengthens** escape time and **raises** the Landauer bill. The result is a Pareto frontier — the **Collaptics uncertainty triangle**:

```
(precision) × (speed) × (1/energy) ≤ κ(substrate)
```

with `κ` fixed by `(ρ₀, ω, T_φ)`. Designing a Collaptics machine = choosing where on this frontier to sit for a given problem class. This is the law that replaces "GHz" as the spec sheet.

---

## Pillar 9 — Sharpened, expanded falsifiability

The framework makes the following testable predictions, each checkable on existing coherent Ising machines, optical annealers, and p-bit arrays:

- **P1 — Inverse-square sharpening:** `σ² ∝ Ω⁻²`. Log–log slope of solution variance vs. coherent drive `= −2`. *(Validated numerically — see `simulation/`.)*
- **P2 — Coherence ≡ temperature:** identical solution statistics whenever `Ω²/D` is matched; raising `ρ` is exchangeable with lowering noise `D`.
- **P3 — Precision ceiling:** no readout beats `Var ≥ 1/(I·Ω²)`.
- **P4 — Quadratic energy advantage:** energy to reach target precision `∝ Ω⁻²` vs. a digital baseline's operation count.
- **P5 — Basin-pull selection:** when two minima compete, landing probability ratio `= Γ₁/Γ₂ = e^(−β(V₁−V₂))·√(det H₂/det H₁)` — *width can beat depth*. Build a deep-narrow vs shallow-wide pair and measure the crossover.
- **P6 — Arrhenius time-to-solution:** `ln τ` linear in `β·ΔV` with slope `1`.
- **P7 — Decoherence-bounded hardness:** the hardest barrier solved scales as `ΔV_max ∝ T_φ`; longer-coherence materials solve strictly harder instances.

Falsification of P1 or P5 on real hardware would refute the framework.

---

## Pillar 10 — Informational Geometry: distance is overlap, not coordinates

Collaptics' state space is **not** configuration space `ℝⁿ`. It is the **statistical manifold** `M` of probability fields, and the right metric on it is *not* Euclidean. Two answers are close not when their coordinates are near, but when **their representing fields overlap**.

**The metric is Fisher–Rao** — the *same* Fisher information that defines `Σ`:

```
g_ij(θ) = E[ ∂_i ln P · ∂_j ln P ]
```

Distance between two candidate answers `A, B` is then the **overlap of their fields**, e.g. the Bhattacharyya / fidelity measure

```
d(A, B) = arccos ∫ √( P_A(x)·P_B(x) ) dx
```

or equivalently the Hellinger / KL divergence. This is the precise content of the intuition:

> The distance between **Berlin** and **Munich** is not 600 km. It is *one minus how much the two probability fields that represent them overlap.* Two answers with disjoint basins are maximally far even if their coordinates coincide; two answers whose fields blur into each other are near even if their coordinates are distant.

**Probability curvature (Amari α-geometry).** `M` carries a pair of dual affine connections. Crucially, the collapse fields `P* ∝ e^(−βV)` form an **exponential family** → the manifold of stationary collapses is **dually flat**, where the generalized **Pythagorean theorem** holds for KL divergence. So the "geometry of possibility" is not a metaphor: it is a curved manifold with a flat collapse-submanifold on which divergences decompose orthogonally.

**Why this unifies the framework:**
- The Collapse Flow lifted to this metric is **natural-gradient descent** `θ̇ = −Ω²·g⁻¹·∇V` — informational gravity is literally **geodesic motion on `M`**.
- `Σ = I·Ω²` is the Fisher metric evaluated at the singularity — the curvature of `M` *is* the resolving power.
- **Prediction P-G (confusability):** two attractors are confused in proportion to their Bhattacharyya overlap, **not** their coordinate distance. Build two deep wells with overlapping vs. disjoint basins at equal coordinate separation; collapse error must track overlap, falsifying any Euclidean model.

---

## Pillar 11 — The Collapse Event Horizon: where collapse becomes irreversible

The original theory's deepest structure was the *Collapse Singularity* (the answer). But one layer was missing between the basin and the singularity — the point of no return. Collaptics adds it, completing a four-level hierarchy:

```
Information Field → Attractor Basin → Collapse Event Horizon → Collapse Singularity
```

**Definition.** The *Collapse Event Horizon* is the boundary beyond which probability can no longer escape a Collapse Singularity within the substrate's coherence window — the surface where **collapse becomes irreversible**.

**It is forced by existing math, not postulated.** Inside a well, the Kramers escape time from depth `V(x)` below the barrier `V_b` is `τ_esc(x) = τ₀·e^(β(V_b − V(x)))`. Escape is possible only while the field stays coherent, i.e. for times `< T_φ` (Pillar 5). The horizon is the level set where escape time equals the coherence time, `τ_esc = T_φ`:

```
V_b − V_h = (1/β)·ln(T_φ/τ₀) = ΔV_max
```

The horizon sits **exactly `ΔV_max` below the barrier top** — the same `ΔV_max` from the decoherence floor. The black-hole analogy becomes literal: just as the Schwarzschild radius is where escape velocity equals `c`, the Collapse Event Horizon is where the thermal fluctuation needed to escape exceeds what the noise budget can supply before decoherence. For a quadratic well `V = ½·λ·r²`, the **collaptic Schwarzschild radius** is

```
r_h = √( 2·(V_b − ΔV_max) / λ )
```

**Consequences (the analogy pays off mathematically):**
- **Irreversibility / arrow of time.** Crossing inward commits the Landauer entropy cost `ΔH`; the collapse cannot be undone without external work (Crooks). The horizon is the thermodynamic point of commitment.
- **No-hair theorem analog.** Inside the horizon the trajectory's future is independent of its past (Markov + trapping): the field **forgets its initial condition**, retaining only the singularity's identity — the informational counterpart of "black holes have no hair."
- **Prediction P-H (horizon existence):** escape probability must drop **super-exponentially** once the field passes `V_h`, and the horizon depth must scale as `V_b − V_h ∝ ln T_φ`. Measurable: vary coherence/observation time, locate where return probability collapses.

This is the missing capstone: *Field → Basin → Horizon → Singularity* is now a rigorous hierarchy, each layer with its own equation.

---

## Synthesis

Collaptics, hardened:

1. **Collapse = Wasserstein gradient flow of informational free energy** (JKO) — collapse is variational inference in hardware (Pillar 1).
2. **Informational gravity = depth × basin-volume**, a real charge `Γ_k` (Pillar 2).
3. **Time-to-collapse `∝ e^(βΔV)`** — an explicit map of where the framework helps and where it does not; an energy/throughput advantage, not a complexity-class change (Pillar 3).
4. **Embedding theorem** — gradient descent, Langevin MCMC, Hopfield, annealing, diffusion models, variational inference, replicator dynamics are all corners of the Collapse Flow (Pillar 4).
5. **`Ω = ρω` derived from classical coherence**, with a **decoherence floor** `ΔV_max ∼ (1/β)·ln(T_φ/τ₀)` answering the analog-noise objection (Pillar 5).
6. **Collapton algebra** — a physically realizable ISA; a program is a coupling graph + drive schedule (Pillar 6).
7. **Error suppression `∝ 1/√N`** — analog robustness by redundancy (Pillar 7).
8. **Thermodynamic triangle** — precision × speed × (1/energy) ≤ κ(substrate), the new spec sheet (Pillar 8).
9. **Seven falsifiable predictions**, two of them framework-sinking (Pillar 9).
10. **Informational geometry** — the state space is the Fisher–Rao statistical manifold; distance between answers is field *overlap*, not coordinates; the collapse fields form a dually-flat manifold (Pillar 10).
11. **The Collapse Event Horizon** — the irreversibility boundary at `V_b − V_h = ΔV_max`, completing the hierarchy *Field → Basin → Horizon → Singularity* and making the black-hole analogy literal (Pillar 11).

The headline identity `Σ = I·Ω²` now sits on a load-bearing structure: a variational principle above it, an information-geometric manifold around it, a complexity boundary beside it, an event horizon within it, a substrate model beneath it, and a falsification program in front of it.
