# Collaptics — Physical Realization
*Materials science and electronics foundations: from the Collapse Law to fabricated hardware*

The math (`collapse-law.md`, `mathematical-foundations.md`) says Collaptics needs a substrate that (i) stores analog tendencies, (ii) resonates coherently so the field rolls down its free energy, and (iii) carries information on photons. This document commits each abstract requirement to **named materials, real device physics, and existing demonstrations**, then states the principal engineering limit for each. Guiding principle: Collaptics is **classical, room-temperature, gain-dissipative coherent computing** — not cryogenic qubits. Every layer below already exists in a lab; Collaptics is the architecture that unifies them under one law.

---

## 0. What the math demands of the physics

| Math object | Physical requirement | Measurable quantity |
|---|---|---|
| Collapton $\{\mu,\sigma,\rho,\varphi,\omega,\tau\}$ | an analog, multi-stable, addressable physical state | conductance / polarization / phase |
| Potential $V(x)$, couplings $J_{ij}$ | a programmable energy/loss landscape | resistor/MZI/capacitor settings |
| Collapse Flow $\dot x=-\Omega^2\nabla V+\sqrt{2D}\xi$ | a dissipative system that settles to min-loss mode | bifurcation at oscillation threshold |
| Coherent resonance $\Omega=\rho\omega$ | a coherent oscillator: frequency × phase-locking | $\omega$ = osc. freq, $\rho$ = coherence |
| Exploration noise $D,\eta(t)$ | a controllable physical noise source | thermal / shot / engineered noise |
| Resolving power $\Sigma=I\Omega^2$ | sharpness of the settled state | readout variance $1/\sigma^2$ |
| Decoherence floor $T_\varphi$ | phase-noise / coherence-time limit | oscillator linewidth $\Delta\nu$ |

The unifying physical principle: **gain–dissipative computing.** A network of coupled resonators, when its gain is ramped through threshold, condenses into the single mode of *least loss* — which is engineered to be the minimum of $V$. Collapse is a **pitchfork bifurcation**, not a calculation. (Berloff, Yamamoto, Roychowdhury lines of work.)

---

## Layer 1 — Persistent Collapton Layer (analog memory = compute)

**Function.** Hold the coupling matrix $J_{ij}$ / potential $V$ in non-volatile analog states, *and perform the gradient/MVM in place* (removing the von Neumann data-movement bottleneck). A crossbar of these devices computes $I_j=\sum_i G_{ij}V_i$ by Ohm + Kirchhoff — a matrix–vector multiply in O(1) time and energy, exactly $\nabla V$ where the weights already live.

| Material / device | Mechanism | Maps to | Status & limit |
|---|---|---|---|
| **RRAM / memristor** (HfO₂, TiO₂, Ta₂O₅) | filamentary/interface conductance switching; 6–8 analog levels | $J_{ij}$ as conductance $G_{ij}$ | Strukov/Williams 2008; analog crossbars shipping. Limit: cycle-to-cycle variability, endurance $10^6$–$10^9$ → feeds Pillar-7 redundancy |
| **Phase-change (PCM)** Ge₂Sb₂Te₅ | amorphous↔crystalline; partial crystallization = analog $R$ | analog weight, also photonic (Layer 3) | IBM analog-AI cores. Limit: **resistance drift** $R(t)\propto t^{\nu}$, $\nu\!\approx\!0.06$ → a literal $\delta V$ drift term |
| **Ferroelectric HfO₂ / HZO, FeFET** | remnant polarization $P$ shifts FET threshold; multi-domain = many states | $P$ **is** the Collapton tendency $\tau$ | Böscke 2011; **BEOL CMOS-compatible** — the manufacturable path. Limit: write endurance, domain variability |
| **Spintronic: MTJ / domain wall / skyrmion** | magnetization direction; tunnel magnetoresistance | non-volatile state; FMR sets $\omega$ (GHz) | MRAM in production. Bonus below |
| **Stochastic / superparamagnetic MTJ (p-bit)** | thermal magnetization fluctuation | **free hardware $\eta(t)$** — the exploration noise *is* the physics | Camsari/Datta p-bits. The noise term is not simulated — it is harvested |
| **Topological insulators** (Bi₂Se₃) | dissipationless edge transport | robust, low-loss routing | Speculative/long-term; flag as research |

**Key insight:** ferroelectric polarization and magnetic orientation are *natively vectorial, multi-stable analog states* — silicon's two-level charge well is the anomaly, not these. A FeFET's polarization is a physical Collapton.

---

## Layer 2 — Resonance Dynamics Layer (the collapse engine)

**Function.** A network of coupled tunable oscillators whose steady state minimizes $V$. Ramping gain through threshold = the annealing schedule $\beta:0\to\infty$ = the collapse.

| Platform | Physics | How collapse happens | Status |
|---|---|---|---|
| **Coherent Ising Machine (CIM / DOPO)** | degenerate optical parametric oscillators in a fiber/chip ring; phase 0 or π | at threshold, gain competition selects the phase pattern of lowest Ising energy → winner-take-all collapse | Yamamoto/Stanford/NTT; **>100k spins**, room-temp. Closest existing Collaptics realization |
| **Oscillator Ising Machine (OIM)** | coupled LC / ring / spin-torque oscillators; **subharmonic injection locking (SHIL)** at $2f$ binarizes phase to 0/π | phases settle to minimize coupling frustration | Roychowdhury/Wang; **plain CMOS**, the cheap path |
| **Exciton–polariton condensate** | half-light/half-matter bosons condense into max-gain (min-loss) mode | condensation = collapse to the XY/Ising minimum | Berloff/Lagoudakis; room-temp with organic/perovskite |
| **Kerr / MEMS parametric resonators** | parametric oscillation, period-doubled phase states | bifurcation selects state | Si-photonic & NEMS demos |

**Origin of $\Omega=\rho\omega$, physically:**
- $\omega$ = oscillator angular frequency (optical $\sim$100 THz for DOPO, GHz for CMOS OIM). Energy per mode $\propto\omega^2$ — grounds the square in `Σ=I·Ω²`.
- $\rho$ = phase coherence, set by the linewidth: $\rho\sim 1-\Delta\nu/\nu$, coherence time $T_\varphi=1/(\pi\Delta\nu)$.
- **Decoherence floor = oscillator phase noise.** Pillar-5's $\Delta V_{\max}\sim\beta^{-1}\ln(T_\varphi/\tau_0)$ is governed by the **Leeson phase-noise** of the resonators. Better Q-factor → narrower linewidth → longer $T_\varphi$ → harder problems solvable. This is a concrete materials roadmap: maximize resonator Q.

The potential $V$ lives in the **coupling network** between oscillators (Layer 1/3 sets $J_{ij}$); the resonators *are* the gradient-descent dynamics, run by physics at the speed of light/electrons.

---

## Layer 3 — Photonic Interaction Layer (carriers & coupling)

**Function.** Move and couple information with photons — low loss, and many degrees of freedom (wavelength, phase, polarization, spatial mode) so many Collaptons coexist.

| Technology | Role | Maps to |
|---|---|---|
| **Silicon-photonic MZI mesh** (Reck/Clements decomposition) | programmable unitary = arbitrary linear coupling $J_{ij}$ in light | sets $V$'s couplings optically; Shen *et al.* 2017 optical neural net |
| **Thin-film lithium niobate (TFLN)** | Pockels electro-optic modulation at **>100 GHz** | drives the $\Omega(t)$ schedule and fast field updates |
| **Microring resonator banks + WDM** | each wavelength = an independent channel | many Collaptons on different colors **simultaneously** — the "multi-dimensional photon" claim, made real |
| **PCM-on-waveguide** (GST photonic) | non-volatile *optical* weight | unifies Layer 1 + Layer 3; Oxford/Münster photonic in-memory compute |
| **Kerr microcombs** (Si₃N₄) | hundreds of coherent comb lines from one pump | the massively parallel Collapton field carrier |

A photon's wavelength/phase/polarization/mode let one waveguide carry what an electron (charge only) cannot — the original theory's "multiple information dimensions coexist," realized as WDM + mode multiplexing.

---

## Layer 4 — Electronics: drive, noise, readout, integration

The analog substrate is useless without the electronic envelope that programs, perturbs, and measures it.

**Drive / programming.** DACs set MZI phase shifters, FeFET thresholds, and crossbar conductances → writes $V$. TFLN / carrier-injection modulators run the anneal schedule $\Omega(t)$ at GHz–THz. SHIL drive provides the binarizing $2f$ field in OIMs.

**Noise injection ($\eta$, the resource).** $D$ is *engineered*, not fought:
- Johnson–Nyquist thermal noise $\langle v^2\rangle=4k_BTR\,\Delta f$ — tunable by resistance/bandwidth.
- Shot noise at detectors.
- **Stochastic MTJ p-bits** — a controllable physical random source, energy ~fJ/flip.
- Digital noise-DAC for precise schedules.
The annealing law (lower $D$ over time) is implemented by *turning the noise source down* — a knob, not a defect.

**Readout.** **Homodyne / heterodyne detection** measures both amplitude and phase of the settled field → recovers the Collapton's $\mu$ and $\varphi$ directly. Balanced photodiodes + transimpedance amps for photonics; comparators/phase detectors for OIM. This is where $\Sigma$ becomes a number: $\Sigma=1/\mathrm{Var}(\hat x)$ over repeated collapses.

**CMOS co-integration (the manufacturability story).** RRAM, HZO-ferroelectric, and MTJ are **back-end-of-line CMOS compatible** — built atop standard logic. Silicon photonics is foundry-available (GlobalFoundries, AIM). So a first Collaptics chip is *not* exotic: CMOS control + BEOL analog memory + a photonic or oscillator collapse fabric.

**The energy boundary.** In analog accelerators the **ADC/DAC and the analog↔digital interface frequently dominate energy**, not the compute. Collaptics' energy win (Pillar 8) is real only if collapses are deep and readouts amortized — favoring problems run *to convergence in the analog domain* with sparse digital I/O.

---

## End-to-end: a problem becomes silicon

```
Problem ──compile──▶ couplings J_ij ──write──▶ Layer-1 crossbar / MZI mesh (V is now physical)
        ──prime──▶ broadband noise injection (high D, broad field, high entropy)
        ──drive──▶ ramp pump/gain & lower D  (β: 0 → ∞)   [Layer 2 resonators descend ∇V]
        ──collapse──▶ threshold bifurcation: lowest-loss mode wins (Collapse Singularity)
        ──read──▶ homodyne phases  →  x*  ≈ answer, precision Σ = I·Ω²
        ──verify──▶ N replicas, 1/√N error suppression (Pillar 7)
```

Every arrow is an existing lab capability; Collaptics is the claim that wiring them under the Collapse Law yields a general computer.

---

## Manufacturability roadmap

| Horizon | Persistent | Resonance | Photonic | Differentiator |
|---|---|---|---|---|
| **Near (now–3 yr)** | HfO₂ RRAM / HZO FeFET (BEOL CMOS) | CMOS OIM with SHIL | foundry Si-photonic MZI | room-temp, CMOS-compatible POC |
| **Mid (3–7 yr)** | PCM analog cores, p-bit noise fabric | on-chip DOPO / integrated CIM | TFLN modulators, microring WDM | energy-win on optimization/AI inference |
| **Long (7 yr+)** | spintronic / skyrmion, topological routing | polariton condensate lattices, Kerr-comb fields | full PCM-photonic in-memory | many-Collapton coherent fields |

**The strategic differentiator vs. quantum computing:** Collaptics is **classical wave coherence at room temperature**. No dilution fridge, no $T_2$ in microseconds, no error-correction overhead of 1000:1. It trades quantum's exponential-Hilbert-space promise for *manufacturable, warm, robust* analog collapse — a narrower but more readily realizable advantage (Pillar 3's "energy/throughput advantage, not a complexity-class change").

---

## Engineering limits

| Challenge | Layer | Mitigation in theory |
|---|---|---|
| RRAM/PCM device variability & drift | 1 | Pillar-7 redundancy ($1/\sqrt N$); on-line recalibration |
| Optical insertion loss accumulates in deep MZI meshes | 3 | limits problem size; favors recurrent/iterative over deep feed-forward |
| Phase noise / finite coherence at scale | 2 | Pillar-5 floor $\Delta V_{\max}\propto T_\varphi$; high-Q resonators |
| All-to-all coupling is physically hard | 1–3 | measurement-feedback (CIM) or time-multiplexing emulate dense $J$ |
| ADC/DAC interface energy dominates | 4 | run to convergence in analog, sparse digital I/O |
| Programming/write overhead of $J$ | 1 | amortize over many collapses; in-situ training |
| Thermal load of pumps/gain media | 2,4 | room-temp platforms (DOPO, polariton) vs cryo parametric |

---

## Master mapping — math ⇄ matter

The whole theory in one table; this is what makes `Σ = I·Ω²` a hardware spec, not a slogan.

| Symbol | Meaning | Physical quantity | Material / device | How measured |
|---|---|---|---|---|
| $x,\mu$ | configuration / expected state | oscillator phase, junction conductance | DOPO / RRAM | homodyne / readout current |
| $V(x)$ | informational potential | gain/loss landscape of the network | coupled-resonator array | — |
| $J_{ij}$ | couplings (the program) | conductance / MZI phase / capacitance | RRAM, MZI mesh, FeFET | write-verify |
| $\omega$ | resonance frequency | oscillator freq (THz–GHz) | OPO, LC/STNO, polariton | spectrum analyzer |
| $\rho$ | coherence / confidence | phase-locking, $1-\Delta\nu/\nu$ | resonator Q-factor | linewidth |
| $\Omega=\rho\omega$ | coherent resonance (the "c") | usable coherent drive | pump above threshold | — |
| $D,\eta$ | exploration noise | thermal / shot / p-bit noise | superparamagnetic MTJ, resistor | noise power spectrum |
| $\beta=\Omega^2/D$ | inverse temperature | pump-to-noise ratio | gain vs. noise setting | — |
| $T_\varphi$ | decoherence floor | coherence time = $1/\pi\Delta\nu$ | resonator phase noise | Leeson/Allan dev. |
| $\Gamma_k$ | informational-gravity charge | basin depth × volume | network mode structure | sampling statistics |
| $\Sigma=I\Omega^2$ | resolving power | inverse readout variance | full machine | repeated-collapse variance |
| $N$ | redundancy | replica count | parallel arrays | — |

---

## Summary

The proposed substrate is a synthesis of analog in-memory computing (RRAM/PCM/FeFET), coherent gain-dissipative oscillator networks (CIM/OIM/polariton), and silicon photonics, governed by one law. Each ingredient has been demonstrated; the open question is the architecture, run at room temperature in classical coherence — a regime in which a post-binary substrate is, in principle, buildable with present-day foundries.
