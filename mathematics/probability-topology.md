# Probability Topology

*How a problem becomes a landscape, and how that landscape decides the answer.*

In Collaptics a problem is encoded as an informational potential `V(x)`. The shape of `V` — its critical points, basins, barriers, and curvature — is what the machine actually computes over. This page collects the topology.

## Critical points are the candidate answers

Every minimum of `V` is a candidate solution (a Collapse Singularity). Maxima and saddles are the barriers between them. By Morse theory, the number and arrangement of these critical points fixes the structure of the whole solution space. The deepest, widest minimum is the dominant answer.

## The partition function

At inverse temperature `β = Ω²/D`, the stationary field is the Gibbs distribution:

```
P*(x) ∝ exp(−β·V(x)),       Z(β) = ∫ exp(−β·V(x)) dx
```

The probability mass that lands in basin `k` follows from Laplace's method:

```
p_k = Z_k / Z,     Z_k = exp(−β·V_k) · (2π/β)^(n/2) · (det H_k)^(−1/2)
```

This is where **informational gravity** gets its formula: each basin pulls in proportion to depth × phase-space volume. A wide shallow basin can beat a deep narrow one.

## Basins, separatrices, horizons

- A **basin** is the set of points that flow to a given minimum under `−∇V`.
- A **separatrix** is the ridge dividing two basins.
- A **Collapse Event Horizon** is the inner level set where escape time exceeds coherence time, `V_b − V_h = β⁻¹·ln(T_φ/τ₀)`. Inside it, the basin membership is committed (see [`../theory/collapse-event-horizon.md`](../theory/collapse-event-horizon.md)).

## The geometry is not Euclidean

Distance between two states is measured on the Fisher–Rao manifold by field overlap, not by coordinates. The Gibbs fields form a dually-flat exponential family on which a KL Pythagorean theorem holds. Full treatment: [`informational-geometry.md`](informational-geometry.md).

## Time on the landscape

Reaching the answer is barrier crossing. The mean first-passage time over a barrier `ΔV` obeys the Arrhenius/Kramers law `τ ∝ exp(β·ΔV)`. Smooth landscapes are crossed cheaply; rugged ones are not. This is the framework's complexity boundary, and it is sharp.

---

See also: [`collapse-law.md`](collapse-law.md) · [`mathematical-foundations.md`](mathematical-foundations.md)
