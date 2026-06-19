# Informational Gravity

*Information bends probability space the way mass bends spacetime.*

Every computational problem, when encoded as a potential landscape `V(x)`, creates distortions in probability space. These distortions form **attractor basins** — regions toward which probability naturally flows. A stronger solution carves a deeper basin.

```
Mass         → bends spacetime
Information  → bends probability space
```

The machine does not search for answers. Answers **pull** the machine toward themselves.

## It is a real charge, not a metaphor

With several candidate solutions `{x_k}`, the amount of probability that flows into basin `k` is given exactly (by Laplace's method) by a **basin pull**:

```
Γ_k  =  exp(−β·V_k)  ·  (det H_k)^(−1/2)
         └─ depth ─┘     └──── width ────┘
```

where `V_k` is the depth of the well, `H_k` its curvature (the Hessian), and `β = Ω²/D` an inverse temperature.

So a basin pulls in proportion to **depth × phase-space volume**. This has a non-obvious consequence:

> A **wide, shallow** attractor can out-pull a **deep, narrow** one.

The strongest solution is not necessarily the deepest — it is the one with the largest `Γ_k`. This prediction is confirmed numerically (test P5a: a shallower-but-wider well wins, 0.394 vs 0.384 — see [`../simulation/RESULTS.md`](../simulation/RESULTS.md)).

## Where it comes from

Informational gravity is geodesic motion on a curved information manifold (the Fisher–Rao manifold; see [`informational-geometry.md`](../mathematics/informational-geometry.md)). The "bending" is the curvature of that manifold, and the curvature at a solution *is* the resolving power `Σ`.

---

Related: [`collapse-singularity.md`](collapse-singularity.md) · [`collapse-event-horizon.md`](collapse-event-horizon.md) · [`informational-collapse.md`](informational-collapse.md)
