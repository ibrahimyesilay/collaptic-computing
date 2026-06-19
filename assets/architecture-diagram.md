# Architecture Diagram

A vector diagram of the proposed substrate is provided alongside this note: [`architecture.svg`](architecture.svg). This page describes what it shows.

## The substrate stack

Collaptics proposes a three-layer physical substrate. Information flows downward through the layers during a computation, and the whole stack is governed by the constitutive law.

```
┌──────────────────────────────────────────────────────────────┐
│  Photonic Interaction Layer                                   │
│  carriers & coupling — MZI mesh, wavelength multiplexing,     │
│  lithium-niobate drive                                        │
├──────────────────────────────────────────────────────────────┤
│  Resonance Dynamics Layer                                     │
│  the collapse engine — coupled oscillators,                   │
│  bifurcation at threshold                                     │
├──────────────────────────────────────────────────────────────┤
│  Persistent Collapton Layer                                   │
│  analog memory = compute — ferroelectric, memristive,         │
│  spintronic states                                            │
└──────────────────────────────────────────────────────────────┘

                  governed by:   Σ = I · Ω²     ( Ω = ρ · ω )
       resolving power = latent information × coherent resonance²
```

## What each layer does

- **Photonic Interaction Layer** — carries Collaptons on light and sets the problem couplings `J_ij`; many Collaptons coexist on different wavelengths. See [`../hardware/photonic-interaction-layer.md`](../hardware/photonic-interaction-layer.md).
- **Resonance Dynamics Layer** — the computational core, where coupled resonators settle into the lowest-loss configuration at threshold; this settling is informational collapse. See [`../hardware/resonance-dynamics-layer.md`](../hardware/resonance-dynamics-layer.md).
- **Persistent Collapton Layer** — stores analog Collapton states and performs the in-place gradient computation. See [`../hardware/persistent-collapton-layer.md`](../hardware/persistent-collapton-layer.md).

## The end-to-end flow

```
problem ─compile→ couplings J_ij ─write→ persistent layer (V is now physical)
        ─prime→   broad, noisy field (high entropy)
        ─drive→   ramp resonance, lower noise   (β: 0 → ∞)
        ─collapse→ threshold bifurcation: lowest-loss mode wins
        ─read→    homodyne detection → answer, precision Σ = I·Ω²
```

Every stage corresponds to a demonstrated laboratory capability; the framework's proposal is the architecture that connects them under one law. See [`../hardware/collaptic-substrate.md`](../hardware/collaptic-substrate.md) for the full treatment.
