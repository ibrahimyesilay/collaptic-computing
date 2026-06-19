# Informational Geometry

*Distance between answers is measured by overlap, not by coordinates.*

In Collaptics, the state space is **not** ordinary coordinate space. It is the **statistical manifold** of probability fields, and distance on it is not Euclidean.

Consider two answers:

```
Berlin        Munich
```

Their distance is **not** 600 kilometers. It is *one minus how much the two probability fields that represent them overlap.* Two answers whose basins are disjoint are maximally far apart even if their coordinates nearly coincide; two answers whose fields blur into each other are close even when their coordinates are distant.

## The metric

The natural metric is the **Fisher–Rao metric** — the same Fisher information that defines the resolving power `Σ`:

```
g_ij(θ) = E[ ∂_i ln P · ∂_j ln P ]
```

Distance between candidate answers `A` and `B` is the **overlap of their fields**, e.g. the Bhattacharyya / fidelity measure:

```
d(A, B) = arccos ∫ √( P_A(x) · P_B(x) ) dx
```

## Probability curvature

The manifold is curved (Amari's α-geometry). Crucially, the collapse fields `P* ∝ exp(−βV)` form an *exponential family*, which makes the manifold of stationary collapses **dually flat** — a space where a generalized Pythagorean theorem holds for the KL divergence.

This is what "the geometry of possibility" means precisely: a curved information manifold with a flat collapse-submanifold, on which:

- **Informational gravity** is geodesic motion,
- **Collapse** is natural-gradient descent (`dθ/dt = −Ω²·g⁻¹·∇V`),
- **Resolving power `Σ`** is the metric evaluated at the singularity.

## Prediction

Two attractors are confused in proportion to their field **overlap**, not their coordinate distance. Build two wells with equal coordinate separation but overlapping vs. disjoint basins; collapse error must track overlap. Any model that uses Euclidean distance is falsified.

---

Related: [`informational-gravity.md`](../theory/informational-gravity.md) · [`../mathematics/probability-topology.md`](probability-topology.md)
