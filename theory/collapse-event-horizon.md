# The Collapse Event Horizon

*The boundary beyond which a collapse can no longer be undone.*

Between the attractor basin and the Collapse Singularity lies one more structure — the point of no return. The **Collapse Event Horizon** is the surface beyond which probability can no longer escape a singularity within the substrate's coherence window. Inside it, collapse becomes **irreversible**.

This completes the hierarchy:

```
Information Field → Attractor Basin → Collapse Event Horizon → Collapse Singularity
```

## It is derived, not postulated

Inside a well, the time for the field to escape from depth `V(x)` below the barrier `V_b` follows the Kramers law:

```
τ_escape(x) = τ₀ · exp( β·(V_b − V(x)) )
```

Escape is only possible while the field stays coherent — for times shorter than the coherence time `T_φ`. The horizon is the level set where these two times are equal:

```
V_b − V_h  =  (1/β)·ln( T_φ / τ₀ )  =  ΔV_max
```

The horizon sits **exactly `ΔV_max` below the barrier top** — the same `ΔV_max` that bounds how hard a problem a given substrate can solve. The black-hole analogy becomes literal: just as the Schwarzschild radius is where escape velocity equals the speed of light, the Collapse Event Horizon is where the thermal kick needed to escape exceeds what the noise budget can supply before the substrate decoheres.

For a quadratic well `V = ½λr²`, the **collaptic Schwarzschild radius** is:

```
r_h = √( 2·(V_b − ΔV_max) / λ )
```

## Why it matters

- **Irreversibility / the arrow of time.** Crossing inward commits the Landauer entropy cost; the collapse cannot be reversed without external work. The horizon is the moment of commitment.
- **A no-hair theorem analog.** Once inside, the trajectory's future is independent of its past — the field *forgets its initial condition*, retaining only the singularity's identity. Black holes have no hair; neither does a committed collapse.

## Prediction

Escape probability must drop *super-exponentially* once the field passes `V_h`, and the horizon depth must scale as `V_b − V_h ∝ ln T_φ`. Vary the coherence/observation time and locate where the return probability collapses.

---

Related: [`collapse-singularity.md`](collapse-singularity.md) · [`informational-collapse.md`](informational-collapse.md) · [`../hardware/collaptic-substrate.md`](../hardware/collaptic-substrate.md)
