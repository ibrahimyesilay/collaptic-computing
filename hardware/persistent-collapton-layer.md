# The Persistent Collapton Layer

*Analog, non-volatile storage of Collapton states — and the place where computation happens.*

This is the memory layer of a Collaptics substrate, but in Collaptics memory and computation are not separate. The same devices that hold the coupling matrix `J_ij` of a problem also perform the operation on it. A crossbar of analog elements computes a matrix–vector product by Ohm's and Kirchhoff's laws — current sums where the weights already live — so the gradient `∇V` is evaluated in place, without moving data to a processor and back. This is the concrete meaning of "removing the von Neumann data-movement bottleneck."

## What this layer must provide

- Many stable, analog levels (not just two), so a device can store a tendency rather than a bit.
- Non-volatility, so a configured problem persists without power.
- In-place computation, so the layer is also the arithmetic.

## Candidate materials

| Material / device | Mechanism | Role in Collaptics | Honest limitation |
|---|---|---|---|
| **RRAM / memristor** (HfO₂, TiO₂, Ta₂O₅) | analog conductance switching, multiple levels | stores `J_ij` as conductance; crossbar does the MVM | device-to-device and cycle-to-cycle variability |
| **Phase-change (PCM)**, Ge₂Sb₂Te₅ | partial crystallization gives analog resistance | analog weight; also usable photonically | resistance drift over time |
| **Ferroelectric HfO₂ / HZO, FeFET** | remnant polarization shifts a transistor threshold | polarization *is* the Collapton tendency; CMOS-compatible | write endurance, domain variability |
| **Spintronic (MTJ, domain wall)** | magnetization direction; tunnel magnetoresistance | non-volatile state; resonance sets a natural frequency | density and write energy |
| **Stochastic / superparamagnetic MTJ** | thermal magnetization fluctuation | a controllable physical noise source — the exploration term `η` for free | requires careful biasing |

A recurring point: ferroelectric polarization and magnetic orientation are *natively* analog and multi-stable. Silicon's clean two-level charge well is the exception among physical states, not the rule.

## Connection to the framework

- The stored conductances/polarizations define the potential `V` and its couplings `J_ij`.
- The crossbar evaluates `∇V` directly — the drift term of the Collapse Flow.
- Stochastic devices can supply the noise term `η` physically, so exploration is harvested from thermal physics rather than computed.
- Device variability and drift are the physical origin of the error term `δV`, suppressed by replica redundancy (`1/√N`).

## Manufacturability

RRAM, HZO-ferroelectric, and MTJ devices are back-end-of-line CMOS compatible — they can be fabricated on top of standard logic. A first substrate need not be exotic: conventional CMOS control with a back-end analog memory fabric is a realistic starting point.

---

Related: [`collaptic-substrate.md`](collaptic-substrate.md) · [`resonance-dynamics-layer.md`](resonance-dynamics-layer.md) · [`photonic-interaction-layer.md`](photonic-interaction-layer.md)
