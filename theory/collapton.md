# The Collapton

*The fundamental information unit of Collaptics.*

A bit is a point: it is `0` or it is `1`. A **Collapton** is a cloud: it stores a *tendency* — an entire probability distribution — rather than a single value.

```
bit:       x = 5
Collapton:  x ≈ { 5 : 71%,  6 : 18%,  4 : 11% }
```

## State

A Collapton is described by six quantities:

```
C = {
  μ : expected state
  σ : uncertainty
  ρ : confidence density
  φ : phase
  ω : resonance signature
  τ : directional tendency
}
```

Two of these — the resonance signature `ω` and the confidence density `ρ` — combine into the **coherent resonance** `Ω = ρ·ω` that governs the entire framework (see [`../mathematics/collapse-law.md`](../mathematics/collapse-law.md)).

## Why a distribution, not a value

Reality is rarely binary. Language, biology, markets, and intelligence operate through probabilities and tendencies. Modern AI already represents everything as probability distributions — but it burns trillions of binary operations to *simulate* them. A Collapton represents the distribution **directly**, in the physical state of the substrate.

## Physical realization

A Collapton is not an abstraction looking for hardware. Several physical states are natively multi-valued and analog — silicon's two-level charge well is the anomaly, not these:

- a **ferroelectric polarization** (continuous, multi-domain),
- a **magnetic orientation** (a vector, with a natural resonance frequency),
- an **optical oscillator phase** (continuous, coherent).

A FeFET's polarization *is* a physical Collapton. See [`../hardware/collaptic-substrate.md`](../hardware/collaptic-substrate.md).

## Algebra

Collaptons compose like a probabilistic graphical model: coupling two Collaptons **adds** their potentials and **multiplies** their fields. A Collaptics program is a coupling graph plus a resonance schedule — not a sequence of instructions.

---

Related: [`informational-collapse.md`](informational-collapse.md) · [`informational-gravity.md`](informational-gravity.md) · [`collapse-singularity.md`](collapse-singularity.md)
