# The Resonance Dynamics Layer

*The collapse engine: a network of coupled oscillators that settles into the answer.*

This is the computational heart of a Collaptics substrate. Instead of voltage switching between `0` and `1`, the machine works through resonance — frequency, phase, interference, amplitude. Rather than switching, the substrate relaxes through its resonant modes, and the pattern it settles into is the solution.

## Collapse is a bifurcation, not a calculation

A network of coupled, gain-driven oscillators sits below threshold in a broad, noisy state. As the gain is ramped through threshold, the modes compete, and the single mode of **least loss** wins and grows — a pitchfork bifurcation. Engineer the loss landscape so the lowest-loss mode is the minimum of `V`, and the winner-take-all event *is* the collapse. Ramping the gain is the annealing schedule `β: 0 → ∞`.

This principle — computing by letting a dissipative system find its minimum-loss configuration — is **gain-dissipative computing**.

## Platforms

**Coherent Ising Machine (CIM).** Degenerate optical parametric oscillators in a fibre or chip ring take phase 0 or π; at threshold the network settles into the phase pattern of lowest Ising energy. Demonstrated past 100,000 spins, at room temperature. The closest existing realization of this layer.

**Oscillator Ising Machine (OIM).** Coupled LC, ring, or spin-torque oscillators, binarized to phase 0/π by subharmonic injection locking at twice the frequency. Builds in plain CMOS — the cheapest path.

**Polariton condensate.** Half-light, half-matter bosons condense into the maximum-gain mode; condensation is collapse to the minimum. Works at room temperature with the right materials.

## Where Ω = ρ·ω comes from

This layer is where the framework's conversion constant becomes physical:

- **ω** is the oscillator frequency — optical (~100 THz) for a CIM, GHz for a CMOS OIM. Energy per mode scales with ω², which is the origin of the square in `Σ = I·Ω²`.
- **ρ** is the phase coherence, set by the resonator linewidth: `ρ ≈ 1 − Δν/ν`, with coherence time `T_φ = 1/(π·Δν)`.

So the usable drive is `Ω = ρ·ω`: high frequency is worthless if it is not phase-locked. Incoherent light (ρ → 0) computes nothing.

## Decoherence is the real limit

The coherence time `T_φ` is set by the resonator's phase noise (Leeson's model). It bounds how hard a problem the substrate can solve: the deepest barrier it can cross before decohering is `ΔV_max ≈ β⁻¹·ln(T_φ/τ₀)`. Higher-Q resonators mean longer `T_φ` mean harder problems — a direct, concrete materials roadmap.

---

See also: [`photonic-interaction-layer.md`](photonic-interaction-layer.md) · [`collaptic-substrate.md`](collaptic-substrate.md) · [`speculative-materials.md`](speculative-materials.md)
