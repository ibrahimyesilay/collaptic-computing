# Collaptic Computing
## A Post-Binary Computational Paradigm Based on Probability Fields, Photonic Resonance, and Informational Collapse

**Author:** Ibrahim Yesilay
**Version:** 1.0.0 · **Year:** 2026 · **License:** CC BY-NC 4.0
**Status:** Theoretical framework. Core predictions reproduced in simulation; no physical prototype yet; built on established physics.

---

### Abstract

For roughly a century, computation has rested on a single, enormously successful abstraction: information represented as discrete binary states. This paper sets out a theoretical alternative. Collaptic Computing represents information not as bits but as continuous probability fields, and it treats computation not as the execution of logic over symbols but as the physical evolution of such a field toward a stable configuration — a process we call informational collapse.

The framework is organized around a single constitutive relation, `Σ = I · Ω²`, where `Σ` is the resolving power of a collapse, `I` is the latent information carried by the field, and `Ω = ρ·ω` is the coherent resonance of the physical substrate (its resonance frequency `ω` weighted by its phase coherence `ρ`). This relation is derived from one stochastic equation of motion and is shown to reproduce, as limiting cases, a range of established computational methods, from gradient descent to Hopfield networks, simulated annealing, and score-based generative models.

Collaptics introduces no new physical law. Every component is anchored to established results in stochastic dynamics, information geometry, statistical mechanics, and condensed-matter device physics. Its contribution is a vocabulary and an organizing principle, together with an explicit and detailed account of where that principle is expected to fail. Six predictions of the constitutive relation are reproduced in a deterministic numerical simulation. The framework is presented as a subject for discussion and falsification, not as a validated technology.

---

## 1. Introduction

### 1.1 The success and the ceiling of binary computing

Every modern processor, memory, network, and machine-learning model ultimately reduces its operation to sequences of two symbols. The binary abstraction succeeded for a clear physical reason: a two-state system is robust against noise. A voltage can drift substantially and still be read correctly as a `0` or a `1`. This noise margin, multiplied across billions of devices, is what made reliable large-scale computation possible.

The abstraction is now approaching physical limits. As transistors shrink toward atomic dimensions, the margins that made binary robust become harder to sustain, and the energy and engineering costs of maintaining clean two-state behaviour grow. The conventional response is to push the same abstraction further: smaller devices, new transistor geometries, three-dimensional integration. This paper asks a different question. Rather than making the switch smaller, what happens if we reconsider the bit itself?

### 1.2 Reality is not binary

The systems we most want to compute over are rarely binary. Natural language is a distribution over possible continuations. Biological folding is a search over a continuous energy landscape. Markets, weather, and perception are matters of tendency and likelihood, not of discrete truth values. Contemporary artificial intelligence already reflects this: a neural network's output is a probability distribution, and the model spends enormous numbers of binary operations simulating that distribution on hardware that is fundamentally ill-suited to it.

Collaptics begins from the premise that information might be represented in a form closer to the phenomena it describes — as a field of probabilities and tendencies — and that some physical substrates are naturally suited to storing and evolving such fields directly, without the intermediate layer of binary simulation.

### 1.3 The thesis

The central hypothesis of Collaptics is compact: *information is not fundamentally a symbol; it can be treated as a physical field, and computation can be carried out by letting that field evolve and collapse.* A Collaptics machine does not execute instructions to arrive at an answer. It is configured so that the answer corresponds to a stable, dominant state of a physical field, and it is allowed to settle into that state.

It is important to be precise about the status of this thesis. Collaptics is not a claim that nature computes this way, nor a claim of a new physical effect. It is a proposal for an architecture and a unifying description, expressed in established physics and mathematics. The remainder of this paper develops the proposal, derives its central relation, situates it among known methods, describes a candidate physical realization, reports numerical checks, and — at equal length — states the conditions under which the framework offers no advantage.

### 1.4 Structure of this paper

Sections 2–3 introduce the fundamental unit (the Collapton), the medium (the informational field), and the mechanism (informational collapse). Section 4 derives the constitutive relation. Sections 5–8 develop the geometry and topology of the framework, including informational gravity, the Fisher–Rao information geometry, the Collapse Singularity, and the Collapse Event Horizon. Section 9 collects the theoretical foundations, relating each claim to an established result. Sections 10–11 describe the proposed physical substrate and a set of more speculative materials. Section 12 reports the numerical validation. Sections 13–14 discuss applications and proposed metrics. Sections 15–17 are devoted to honest boundaries, the falsifiability programme, and a roadmap. Section 18 concludes.

---

## 2. The Collapton and the Informational Field

### 2.1 The Collapton

The fundamental unit of Collaptics is the **Collapton**. Where a bit holds one of two values, a Collapton holds a *tendency* — an entire probability distribution. A classical variable might take the value `x = 5`; the corresponding Collapton expresses something like `x ≈ {5 : 71%, 6 : 18%, 4 : 11%}`. Information ceases to be a point and becomes a localized cloud of possibility.

A Collapton is characterized by six quantities:

```
C = { μ, σ, ρ, φ, ω, τ }
```

the expected state `μ`, the uncertainty `σ`, the confidence density `ρ`, the phase `φ`, the resonance signature `ω`, and the directional tendency `τ`. Two of these — the resonance signature `ω` and the confidence density `ρ` — combine into the quantity that governs the entire framework, the coherent resonance `Ω = ρ·ω`.

The Collapton is not an abstraction in search of an implementation. Several physical states are natively analog and multi-valued: the polarization of a ferroelectric domain, the orientation of a magnetic moment, the phase of an optical oscillator. In each case the physical state can take many stable values rather than two. Viewed this way, silicon's clean two-level charge well is the unusual case among physical systems, not the norm.

### 2.2 The informational field

A single Collapton expresses one local tendency. A computation involves many, and together they constitute an **informational field**: a probability density `P(x, t)` defined over the space of candidate configurations `x`. The field is the medium of Collaptics in the same sense that an electromagnetic field is the medium of an electromagnetic process. It assigns a probability to every candidate answer, and it carries not just the candidates but their relative weights, correlations, and uncertainties simultaneously.

Computation, in Collaptics, is the controlled evolution of this field. The state of the field at any instant represents the machine's complete current knowledge of the problem; the field's eventual concentration onto a dominant configuration is the answer. The full treatment is in [`../theory/informational-field.md`](../theory/informational-field.md).

### 2.3 Composition

Collaptons compose in the manner of a probabilistic graphical model. Coupling two Collaptons adds their potentials and multiplies their fields. As a consequence, a Collaptics "program" is not a sequence of instructions but a coupling graph — a specification of how the Collaptons influence one another — together with a schedule for the drive that anneals the system from exploration toward commitment. This shifts the act of programming from describing *how* to compute toward describing *what* landscape the field should settle within.

---

## 3. Informational Collapse

### 3.1 The mechanism

The defining process of Collaptics is informational collapse. The contrast with classical computation is stark:

```
Classical:  Input → Instructions → Output
Collaptics:        Probability Field → Resonance → Attractor → Collapse → Emergent Solution
```

The system begins in a broad, high-entropy state in which an enormous number of candidate solutions coexist. Under the combined influence of the substrate's resonance and the structure of the problem, the field reorganizes itself, concentrating probability and shedding entropy, until it settles onto one dominant configuration. That settling is the answer. The machine does not search through candidates one at a time; it lets the entire field flow toward the dominant attractor.

### 3.2 The equation of motion

The whole framework rests on a single equation, the **Collapse Flow**:

```
dx/dt = −Ω²·∇V(x) + √(2D)·ξ(t)
```

Here `V(x)` is the informational potential — the problem encoded as a landscape, with low regions corresponding to good solutions — and `ξ(t)` is a white-noise term. The first term drives the field downhill along the gradient of `V`, at a rate set by the squared coherent resonance `Ω²`. The second term injects controlled noise of strength `D`.

The single assumption unique to Collaptics is the identification of the substrate's coherent resonance `Ω` with the mobility of this gradient flow: a more coherent, higher-frequency substrate drives the field downhill more strongly. Everything that follows is a consequence of this one identification combined with standard results.

### 3.3 Noise as a resource

In binary computing, noise is the adversary. In Collaptics, the noise term is functional. It is the mechanism by which the field explores, escaping shallow features of the landscape that are not the true solution. The ratio `Ω²/D` plays the role of an inverse temperature: increasing coherence is equivalent to cooling the field, sharpening it toward the deepest attractor; increasing noise is equivalent to heating it, restoring exploration. A Collaptics computation is, in effect, a physical annealing schedule expressed through this ratio.

### 3.4 The limits of collapse

Collapse reaches the correct answer only when the field can actually traverse the landscape — when it can cross the barriers that separate one basin from another. When those barriers are high, the field becomes trapped in a sub-optimal region and the collapse converges on the wrong configuration. This is not a peripheral caveat; it is the central boundary of the framework, and Section 9 makes it quantitative. Collaptics offers an advantage on landscapes that are smooth enough to traverse, and no advantage on landscapes that are not. The full treatment is in [`../theory/informational-collapse.md`](../theory/informational-collapse.md).

---

## 4. The Collapse Law

This section summarizes the derivation of the constitutive relation. The complete treatment, with every step, is given in [`../mathematics/collapse-law.md`](../mathematics/collapse-law.md).

### 4.1 From trajectories to fields

The Collapse Flow describes the path of a single representative state. The ensemble of all such paths is described equivalently by the evolution of the informational field `P(x, t)`, which obeys the Fokker–Planck equation

```
∂P/∂t = ∇·[ Ω²·(∇V)·P + D·∇P ].
```

This is the field-level law of Collaptics. The drift term concentrates probability at the minima of `V`; the diffusion term spreads it; their balance produces the characteristic behaviour of collapse.

### 4.2 The stationary field

Setting the time derivative to zero and requiring zero probability flux yields the stationary distribution

```
P*(x) ∝ exp[ −(Ω²/D)·V(x) ].
```

This is the central result of the static theory. The factor `β ≡ Ω²/D` occupies exactly the position of an inverse temperature in statistical mechanics. Coherent resonance therefore acts as a cooling parameter: as `Ω` increases, the stationary field becomes ever more sharply peaked on the deepest minimum of `V`. The phrase "the machine converges rather than computes" has, in this expression, a precise meaning.

### 4.3 The geometry of the answer

Expanding the potential around its dominant minimum `x*` (where the gradient vanishes) gives, to second order,

```
V(x) ≈ V(x*) + ½·(x − x*)ᵀ·H·(x − x*),
```

with `H` the curvature (Hessian) of the attractor. The stationary field is then a Gaussian centred on `x*`, and its width along a curvature mode `λ` is

```
σ² = D / (Ω²·λ),     so     σ² ∝ 1/Ω².
```

The collapsed answer becomes quadratically sharper as coherent resonance rises.

### 4.4 The constitutive relation

Define the **resolving power** `Σ` as the precision (inverse variance) with which the field pins down the answer — equivalently, the Fisher information the field carries about `x*`:

```
Σ ≡ 1/σ² = (λ/D)·Ω².
```

Identifying the problem-intrinsic factor `I := λ/D` — the ratio of attractor curvature to exploration noise, which is itself an information quantity — gives the constitutive relation:

```
Σ = I · Ω².
```

The resolving power of a collapse equals the latent information of the field, set by the problem's geometry and the noise budget, multiplied by the square of the substrate's coherent resonance, set by the hardware. The problem contributes linearly; the coherent, resonant collapse contributes quadratically. The square is not stylistic: it appears for the same reasons it appears in the energy of a resonant mode (proportional to frequency squared), in the intensity of a coherent field (proportional to amplitude squared), and in the coupling energy of Hopfield–Ising landscapes (quadratic in the coupling strength).

### 4.5 Immediate consequences

Three results follow directly. First, by the Cramér–Rao inequality, any readout of the answer obeys `Var(x̂) ≥ 1/Σ = 1/(I·Ω²)`; the resolving power is a hard lower bound on achievable error, not a figure of speech. Second, by Landauer's principle, the entropy reduction of a collapse carries a minimum thermodynamic cost; the framework inherits a real energy floor and does not promise free computation. Third, the relation interpolates cleanly between known regimes: as `Ω → 0` the stationary field flattens to undirected search, and as `Ω` grows large with low noise it approaches a deterministic descent.

---

## 5. Probability Topology

A problem in Collaptics is an informational potential `V(x)`, and the structure of that potential — its critical points, basins, barriers, and curvature — is what the machine computes over. The full treatment is in [`../mathematics/probability-topology.md`](../mathematics/probability-topology.md).

Every minimum of `V` is a candidate solution; maxima and saddles are the barriers between them. By Morse theory, the number and arrangement of these critical points fix the structure of the solution space. The deepest and widest minimum is the dominant answer.

At inverse temperature `β = Ω²/D`, the probability mass that settles into a given basin follows from Laplace's method. For basin `k` with depth `V_k` and curvature `H_k`, the contribution to the partition function is

```
Z_k = exp(−β·V_k)·(2π/β)^(n/2)·(det H_k)^(−1/2),
```

and the basin's share of probability is `Z_k / Z`. This is the formula from which informational gravity (Section 6) is read off: a basin attracts probability in proportion to its depth and its phase-space volume.

The landscape also fixes the time a computation takes. Reaching the dominant minimum is a matter of crossing barriers, and the mean first-passage time over a barrier of height `ΔV` follows the Arrhenius–Kramers law `τ ∝ exp(β·ΔV)`. Smooth landscapes are crossed cheaply; rugged ones are not. This is the framework's complexity boundary, and it is sharp.

---

## 6. Informational Gravity

The framework's organizing image is that information bends probability space the way mass bends spacetime: a problem, encoded as a potential, creates distortions toward which probability flows. The machine does not search for answers so much as answers draw the field toward themselves.

This image is made quantitative by the basin-pull defined in the previous section:

```
Γ_k = exp(−β·V_k) · (det H_k)^(−1/2).
```

A basin pulls in proportion to **depth × phase-space volume**. The non-obvious consequence is that a wide, shallow basin can out-pull a deep, narrow one: the strongest attractor is not necessarily the deepest, but the one with the largest `Γ_k`. This prediction is confirmed in simulation (Section 12, prediction P5a), where a shallower but wider well captures more probability than a deeper but narrower competitor.

Informational gravity is not a separate force added to the framework; it is geodesic motion on the curved information manifold described in Section 7. The "bending" is the curvature of that manifold, and the curvature at a solution is precisely the resolving power `Σ`. The detailed account is in [`../theory/informational-gravity.md`](../theory/informational-gravity.md).

---

## 7. Informational Geometry

A subtle but important point is that the natural geometry of Collaptics is not Euclidean. The state space is not ordinary coordinate space but the **statistical manifold** of probability fields, and distance on it is measured by overlap, not by coordinates.

Consider two candidate answers, "Berlin" and "Munich." Their separation in Collaptics is not the geographic distance between them. It is one minus the degree to which the two probability fields that represent them overlap. Two answers whose basins are disjoint are maximally far apart even if their coordinates nearly coincide; two answers whose fields blur into one another are close even when their coordinates are distant.

The appropriate metric is the **Fisher–Rao metric** — the same Fisher information that defines the resolving power `Σ`:

```
g_ij(θ) = E[ ∂_i ln P · ∂_j ln P ].
```

The distance between two candidate fields `A` and `B` is then a measure of their overlap, such as the Bhattacharyya or fidelity measure `d(A, B) = arccos ∫ √(P_A · P_B) dx`.

This manifold is curved, in the sense of Amari's information geometry. Crucially, the stationary collapse fields `P* ∝ exp(−βV)` form an exponential family, which makes the submanifold of stationary collapses *dually flat* — a space on which a generalized Pythagorean theorem holds for the Kullback–Leibler divergence. This is the precise content of the phrase "the geometry of possibility": a curved information manifold with a flat collapse-submanifold, on which informational gravity is geodesic motion, collapse is natural-gradient descent, and the resolving power is the metric evaluated at the singularity. The full development is in [`../mathematics/informational-geometry.md`](../mathematics/informational-geometry.md).

---

## 8. The Collapse Singularity and the Collapse Event Horizon

### 8.1 The singularity

At the centre of every problem lies the **Collapse Singularity**, the dominant minimum of `V` — the answer. The analogy with a black hole can be made precise within the framework: a black hole does not compute where matter should go; it curves spacetime so that matter falls inward. Likewise, the strongest solution becomes the deepest informational well, and probability flows toward it.

A singularity is not merely deep; it is the attractor of largest basin-pull `Γ_k`, combining depth and width. Many singularities can coexist in one substrate, and the number of stable singularities per unit volume is one of the metrics Collaptics proposes (Section 14).

### 8.2 The hierarchy and the missing layer

Between the broad field and the singularity, the framework identifies four nested structures:

```
Informational Field → Attractor Basin → Collapse Event Horizon → Collapse Singularity
```

The field is the high-entropy cloud; a basin is a region that drains toward one answer; the singularity is the bottom of the well. The layer that completes the picture is the **Collapse Event Horizon**: the boundary beyond which a collapse can no longer be reversed.

### 8.3 The event horizon, derived

The event horizon is not postulated; it follows from results already in hand. Inside a well, the time for the field to escape from depth `V(x)` below the barrier `V_b` follows the Kramers law, `τ_escape(x) = τ₀·exp(β·(V_b − V(x)))`. Escape is possible only while the field remains coherent — for times shorter than the coherence time `T_φ`. The horizon is the level set where these two times are equal:

```
V_b − V_h = (1/β)·ln(T_φ / τ₀) = ΔV_max.
```

The horizon sits exactly `ΔV_max` below the barrier — the same quantity that, in Section 9, bounds how hard a problem a given substrate can solve. The black-hole analogy becomes precise: just as the Schwarzschild radius is where escape velocity equals the speed of light, the Collapse Event Horizon is where the thermal fluctuation required to escape exceeds what the noise budget can supply before the substrate decoheres.

Two consequences are worth noting. First, crossing inward commits the thermodynamic (Landauer) cost of the collapse; the answer cannot be undone without external work, so the horizon is the point of commitment and the origin of the framework's arrow of time. Second, once inside the horizon the trajectory's future is independent of its past — the field forgets its initial condition, retaining only the identity of the singularity. This is a direct analog of the no-hair property of black holes. The detailed treatment is in [`../theory/collapse-event-horizon.md`](../theory/collapse-event-horizon.md).

---

## 9. Theoretical Foundations

The constitutive relation sits on a structure of established results. Each item below is the load-bearing anchor for a part of the framework; the full development, with references to the underlying theorems, is in [`../mathematics/mathematical-foundations.md`](../mathematics/mathematical-foundations.md).

**Collapse as free-energy descent.** The Collapse Flow is the steepest-descent (Wasserstein) gradient flow of the informational free energy `F[P] = ⟨V⟩ − (1/β)·H[P]`, by the theorem of Jordan, Kinderlehrer, and Otto. The unique minimizer is the Gibbs field. In this sense Collaptics is a physical realization of variational inference: it minimizes a free energy that trades fit against entropy, exactly the objective of approximate Bayesian inference and the free-energy principle.

**Informational gravity as a charge.** The basin-pull `Γ_k` combines depth and phase-space volume, so that the selection of a solution is governed by a well-defined quantity, and width can compete with depth.

**Time-to-collapse and the honest boundary.** The Kramers law gives `τ ∝ exp(β·ΔV)`. This yields an explicit map of where the framework helps and where it does not: smooth, low-barrier landscapes yield large efficiency gains; rugged or worst-case landscapes yield none; landscapes with no usable gradient yield nothing at all.

**An embedding of known methods.** A range of established techniques are special cases of the Collapse Flow: deterministic gradient descent (no noise), Langevin Monte Carlo (its discretization), Hopfield networks and Ising machines (a quadratic potential over discrete states), simulated annealing (a schedule on `β`), score-based diffusion generative models (a learned potential), and natural-gradient variational inference (the flow lifted to the Fisher metric). Collaptics' claim is therefore not to compete with these methods but to describe their common, continuous-time, hardware-native limit.

**The substrate parameter and a decoherence floor.** The coherent resonance `Ω = ρ·ω` follows from classical wave coherence, and finite coherence imposes a ceiling on solvable problem hardness, `ΔV_max ≈ (1/β)·ln(T_φ/τ₀)`. Better coherence purchases harder problems. This is the quantitative answer to the objection that analog noise is fatal: noise does not destroy the framework, it bounds the difficulty a given substrate can handle.

**Error suppression by redundancy.** Device imperfections corrupt the potential by some `δV`. Running `N` independent replicas of a problem averages these independent errors, suppressing the misplacement of the singularity as `1/√N` — the analog counterpart of redundancy-based error correction.

**A thermodynamic triangle.** Precision (Cramér–Rao), speed (Kramers), and energy (Landauer) cannot be jointly maximized; they trade off along a frontier fixed by the substrate. This frontier, rather than clock frequency, is the natural specification for a Collaptics machine.

**Information geometry and the event horizon.** The two structures of Sections 7 and 8 — the Fisher–Rao manifold and the irreversibility boundary — complete the foundations, giving the framework a geometry around its central relation and a point of commitment within it.

---

## 10. Physical Realization

Collaptics is described as classical, room-temperature, gain-dissipative coherent computing, distinct from cryogenic qubit-based approaches. The proposed substrate has three layers; every ingredient named below is a demonstrated laboratory capability, and the framework's proposal is the architecture that connects them. The complete treatment is in [`../hardware/collaptic-substrate.md`](../hardware/collaptic-substrate.md).

### 10.1 The persistent collaptic layer

This layer stores the problem and performs the computation in the same place. A crossbar of analog devices computes a matrix–vector product by Ohm's and Kirchhoff's laws, evaluating the gradient where the weights already reside and removing the need to shuttle data to a separate processor. Candidate devices include resistive memory (RRAM), phase-change materials, ferroelectric field-effect transistors (which are CMOS-compatible), and magnetic tunnel junctions. Stochastic magnetic junctions can supply the exploration noise physically, so the noise term of the Collapse Flow is harvested from thermal physics rather than synthesized. Device variability and drift are the physical origin of the error term `δV`, addressed by the redundancy described in Section 9. The full treatment is in [`../hardware/persistent-collapton-layer.md`](../hardware/persistent-collapton-layer.md).

### 10.2 The resonance dynamics layer

This is the computational core. A network of coupled, gain-driven oscillators sits below threshold in a broad, noisy state; as the gain is ramped through threshold, the modes compete and the single mode of least loss grows and wins. Engineered so that the lowest-loss mode is the minimum of `V`, this winner-take-all event is the collapse, and the gain ramp is the annealing schedule. Coherent Ising machines, oscillator Ising machines, and polariton condensates are existing realizations of this principle. The coherent resonance `Ω = ρ·ω` becomes physical here: `ω` is the oscillator frequency and `ρ` is the phase coherence set by the resonator's linewidth, with the decoherence floor governed by phase noise. The full treatment is in [`../hardware/resonance-dynamics-layer.md`](../hardware/resonance-dynamics-layer.md).

### 10.3 The photonic interaction layer

Photons carry information with low loss and across many degrees of freedom — wavelength, phase, polarization, and spatial mode — so that many Collaptons coexist on one waveguide. Programmable interferometer meshes set the problem couplings optically; high-speed electro-optic modulators drive the annealing schedule; wavelength multiplexing provides parallel channels. Readout is by homodyne detection, which recovers the phase and amplitude of the settled field and so yields a sample from it. The full treatment is in [`../hardware/photonic-interaction-layer.md`](../hardware/photonic-interaction-layer.md).

### 10.4 Manufacturability and honest costs

Several of the persistent-layer devices are back-end-of-line CMOS compatible, and photonic meshes are available from established foundries, so a first substrate need not be exotic. Two honest costs must be stated. Optical loss accumulates through deep interferometer meshes, which caps problem size and favours iterative over deep feed-forward encodings. And the analog-to-digital interface can dominate energy if readouts are frequent, which favours problems run to convergence in the analog domain with sparse input and output.

---

## 11. Speculative Substrates

Beyond the demonstrated materials, the framework admits a wider design space, treated in [`../hardware/speculative-materials.md`](../hardware/speculative-materials.md). These concepts are not buildable today; each is presented with a real physical kernel and a clearly marked speculative step, and each is an attempt to push one term of the constitutive relation to a frontier current hardware cannot reach. They include volumetric collapse in rare-earth-doped crystals (long coherence and large spectral capacity), photorefractive holography (dense all-to-all coupling), room-temperature magnon condensates (warm coherence), photonic time crystals (a new drive mechanism), topologically protected encodings (robustness), reaction–diffusion and liquid-crystal media (self-organizing soft matter), molecular folding substrates (native energy-landscape problems), and plasmonic lattices (information density). The purpose of this catalogue is to show that "abandon the bit" has many independent physical routes, as a paradigm rather than a single device should. One entry — an analog-gravity asymptote — is explicitly fenced off as a thought experiment rather than a device proposal.

---

## 12. Numerical Validation

The framework's predictions are checked by a deterministic, pure-Python (numpy-only) simulation of the Collapse Flow, provided in [`../simulation/`](../simulation/). The simulation does not test any physical claim; it verifies that the equations behave as the framework asserts and reproduce known results of stochastic dynamics. The checks can be reproduced with `python3 test_predictions.py`.

| Prediction | Claim | Result |
|---|---|---|
| **P1** | Resolving power sharpens as `σ² ∝ Ω⁻²` | log–log slope **−1.989** (target −2.000) |
| **P2** | `Ω²/D` is an inverse temperature | variance spread **0.20 %** across matched pairs |
| **P3** | Cramér–Rao ceiling `Var ≥ 1/(I·Ω²)` | measured `Σ = 9.033` vs theory `9.000`; the mean estimator achieves the bound, the median does not beat it |
| **P5a** | Basins select by depth × width; width can beat depth | `P(left) = 0.394` vs Laplace `0.384`; the shallow-wide well wins |
| **P5b** | High barriers trap the field | zero basin crossings; the field does not reach the equilibrium answer |
| **P6** | Time-to-solution `τ ∝ exp(βΔV)` | `ln τ` vs `β·ΔV` slope **0.991** (target 1.000) |

Two of these results are of particular importance. Prediction P3 closes the loop on the constitutive relation: the measured Fisher information of the collapse equals `I·Ω²` and sets a Cramér–Rao accuracy ceiling that the efficient (mean) estimator saturates and no estimator beats. Predictions P5b and P6 are equally important in the opposite direction: they reproduce the framework's failure mode, in which a high barrier traps the field and the answer is not reached, in exact accordance with the exponential Kramers timing. The same simulator therefore demonstrates both where the framework works and where it does not. Reference numbers and a reproduction guide are in [`../simulation/RESULTS.md`](../simulation/RESULTS.md) and [`../simulation/README.md`](../simulation/README.md).

---

## 13. Applications

The following are candidate framings, not demonstrated systems. In every case the realistic claim is narrow and is paired with the conditions under which it fails. Detailed discussions are in [`../examples/`](../examples/).

**Artificial intelligence and language models.** A model's next-token distribution is exactly the kind of object Collaptics represents natively, and the embedding of Section 9 shows that score-based diffusion sampling is a discretized form of the Collapse Flow. The plausible contribution is energy efficiency in inference and sampling over the smooth, learned landscapes that training produces — not a replacement for neural networks, and not a benefit on adversarial or flat landscapes. See [`../examples/ai-inference.md`](../examples/ai-inference.md).

**Combinatorial optimization.** This is the most direct fit, and the one the existing Ising-machine literature already supports: an energy-efficient route to good approximate solutions on structured instances. The framework does not change complexity classes; worst-case hard instances remain hard. See [`../examples/optimization.md`](../examples/optimization.md).

**Protein folding.** Folding is energy minimization, which is the shape of collapse. The framing reframes the problem as a physical descent, with the usual caveats of local minima and barrier height applying directly. See [`../examples/protein-folding.md`](../examples/protein-folding.md).

**Robotics and control.** Perception and decision can be cast as coupled fields that continuously re-converge as the environment changes, yielding emergent, low-latency, low-energy control on smooth action landscapes — but not deliberative planning over rugged decision trees. See [`../examples/robotics.md`](../examples/robotics.md).

**A deliberate negative result.** Cryptographic hash inversion is included precisely because it does *not* work: a secure hash is engineered to have no exploitable gradient, so there is no attractor to collapse into and the process reduces to undirected search. Retaining this case is part of the framework's discipline. See [`../examples/hash-inversion.md`](../examples/hash-inversion.md).

---

## 14. Metrics

If computation is collapse rather than instruction execution, then clock frequency and operation counts are not the natural figures of merit. The framework proposes two metrics in their place.

**Collapse Throughput (CT)** is the rate at which resolving power is produced, `CT = dΣ/dt`. Because `Σ` is a measurable inverse variance over repeated collapses, CT is an operationally defined quantity: the volume of probability space that can be resolved per unit time.

**Singularity Density (SD)** is the number of stable Collaptic Singularities that can coexist within a unit volume of substrate. It captures how many independent problems, or how large a single problem, a given physical medium can hold.

Together these reframe the central engineering question from "how many operations per second" to "how much probability can be shaped, and how finely, per unit time and volume."

---

## 15. Honest Boundaries

**What Collaptics is.** A theoretical framework for describing probabilistic and analog computation; a single constitutive relation with a derivation, a stated domain of validity, and falsifiable predictions, six of which are reproduced in simulation; and a candidate architecture expressed entirely in established physics.

**What Collaptics is not.** It is not new physics, not a physical prototype, not an experimentally validated device, and not a replacement for any existing paradigm. It is not a quantum computer: it relies on classical wave coherence at room temperature, not on qubit superposition or entanglement, and it makes no claim of quantum speedup.

**Current status.** No hardware has yet been built. The validation to date is mathematical and numerical: the simulations confirm internal consistency and agreement with established results. The mapping from the framework to a working machine remains to be carried out.

**Where it may fail.** The advantage depends on a traversable landscape. Time-to-collapse grows exponentially with barrier height, so on rugged, glassy, or worst-case combinatorial problems the framework offers no asymptotic advantage, and on gradient-free problems it offers none at all. The output is the reachable attractor, which may be a local rather than global optimum, so the framework yields good candidates rather than certificates of optimality.

**Why hash inversion is not a guaranteed use case.** Because a secure hash deliberately destroys the gradient structure the framework exploits. With a flat potential there is no basin and no collapse, only search. If the framework could invert a secure hash, that hash would already be broken by ordinary gradient methods.

**Why it is currently theoretical.** For all of the above reasons. The appropriate response to this document is to test and challenge it, not to adopt it.

---

## 16. Falsifiability

Collaptics states predictions that can be checked, several on existing coherent hardware (Ising machines, optical annealers, probabilistic-bit arrays):

- **P1.** Solution variance scales as `Ω⁻²`; the log–log slope must be `−2`. *(Reproduced numerically.)*
- **P2.** Solution statistics are invariant under matched `Ω²/D`; coherence and temperature are interchangeable. *(Reproduced numerically.)*
- **P3.** No readout beats `Var ≥ 1/(I·Ω²)`. *(Reproduced numerically.)*
- **P5.** Basin selection follows depth × width, so a wider, shallower well can win. *(Reproduced numerically.)*
- **P6.** Time-to-solution scales as `exp(β·ΔV)`; `ln τ` is linear in `β·ΔV` with unit slope. *(Reproduced numerically.)*
- **P7.** The hardest solvable barrier scales with coherence time, `ΔV_max ∝ ln T_φ`; longer-coherence substrates solve strictly harder instances. *(Testable on hardware.)*
- **P-G.** Confusability between two attractors tracks the overlap of their fields, not their coordinate distance. *(Testable on hardware.)*
- **P-H.** Escape probability drops super-exponentially past the event horizon, whose depth scales with `ln T_φ`. *(Testable on hardware.)*

Failure of P1 or P5 on physical hardware would falsify the framework.

---

## 17. Roadmap

The framework suggests a staged path, with each stage testable and each building on demonstrated capability rather than on the stages after it.

- **Near term.** Assemble a room-temperature proof of concept from CMOS oscillator Ising machines, back-end analog memory, and foundry silicon photonics, and test predictions P1, P5a, and P6 on silicon.
- **Medium term.** Integrate optical parametric oscillators, physical noise sources, and high-speed electro-optic drive, and seek energy advantages on real optimization and inference workloads.
- **Long term.** Pursue dense all-to-all coupling and volumetric, many-Collapton coherent media drawn from the speculative-materials catalogue.

The strategic position is modest and explicit. Quantum computing bets on an exponentially large state space at the cost of millikelvin operation and heavy error-correction overhead. Collaptics bets instead on classical coherence at room temperature: a narrower advantage, confined to a particular class of problems, but one that can in principle be built with present-day foundries. The framework is offered in that spirit — as a question about whether the bit must remain the unit of information, posed precisely enough to be answered.

---

## 18. Conclusion

Collaptic Computing proposes that information be treated as a physical probability field and that computation be carried out by letting that field collapse toward a stable configuration. From a single equation of motion it derives a constitutive relation, `Σ = I · Ω²`, that ties the accuracy of a result to the coherent resonance of the substrate, and it situates that relation within a structure of established theorems — a variational principle above it, an information-geometric manifold around it, a complexity boundary beside it, an event horizon within it, and a materials stack beneath it. Six of its predictions are reproduced in simulation, including the predictions that mark its own limits.

The framework makes no claim to new physics, to experimental validation, or to a physical prototype, and it states at length the conditions under which it offers no advantage. A classical computer executes logic; Collaptic Computing proposes to shape the geometry of possibility until a single configuration remains — and it states precisely how far that proposal can be taken.

---

## Appendix A — Notation

| Symbol | Meaning |
|---|---|
| `x` | system configuration (a candidate solution) |
| `P(x,t)` | informational field — probability density over configurations |
| `V(x)` | informational potential (the problem as a landscape) |
| `J_ij` | couplings between Collaptons (the program) |
| `ω` | resonance frequency of the substrate |
| `ρ` | confidence density / phase coherence |
| `Ω = ρ·ω` | coherent resonance (the conversion constant) |
| `D` | exploration noise power |
| `β = Ω²/D` | inverse temperature |
| `H` | curvature (Hessian) of an attractor |
| `Γ_k` | basin-pull of singularity `k` (informational-gravity charge) |
| `T_φ` | coherence time (decoherence floor) |
| `ΔV_max` | maximum solvable barrier height |
| `Σ = I·Ω²` | resolving power (the Collapse Law) |
| `CT = dΣ/dt` | Collapse Throughput |
| `N` | replica count for error suppression |

## Appendix B — Background literature

Collaptics builds on, and is intended to be read against, the following established results and bodies of work. These are the foundations to which the framework's claims are anchored; none of them is itself a claim of Collaptics.

- Stochastic dynamics and the Fokker–Planck / Langevin description of overdamped systems.
- H. Kramers (1940), on reaction rates and barrier crossing.
- R. Landauer (1961), on the thermodynamic cost of information erasure.
- J. Hopfield (1982), on associative memory as relaxation to energy minima.
- C. Jarzynski (1997) and G. Crooks (1999), on nonequilibrium work and fluctuation theorems.
- R. Jordan, D. Kinderlehrer, and F. Otto (1998), on the Fokker–Planck equation as a gradient flow of free energy in Wasserstein space.
- S. Amari, on information geometry and the Fisher–Rao metric, including dually flat structures and the generalized Pythagorean theorem.
- The literature on coherent Ising machines, oscillator-based Ising machines, memristive in-memory computing, photonic computing, and probabilistic (p-bit) hardware, as the demonstrated platforms the proposed substrate would unify.

Readers are encouraged to consult these primary sources directly and to judge the framework against them.
