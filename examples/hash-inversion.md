# Example: Hash Inversion — an honest negative result

It is tempting to imagine Collaptics inverting a cryptographic hash: turn the target hash into a probability topology, let the candidate space flow downhill, and watch the field collapse onto the preimage. This does not work, and the reason is instructive: it is the same property that lets Collaptics work elsewhere.

## The setup

Inverting SHA-256 means finding an input `x` such that `SHA256(x) = h` for a given target `h`. The naive idea: encode "distance from the target hash" as a potential `V(x)` over the candidate space, and run the Collapse Flow.

## Why it fails

A cryptographic hash is *designed* to destroy exactly the structure Collaptics exploits.

- **No gradient.** The avalanche property guarantees that flipping one input bit changes about half the output bits. Neighboring inputs produce completely unrelated outputs. So `V(x)` is **flat** — there is no slope pointing toward the answer.
- **No basin.** With a flat landscape, every basin pull `Γ_k` is identical. There is no Collapse Singularity to fall into.
- **Collapse becomes random search.** With `Ω` providing no usable drift over a flat `V`, the Collapse Flow reduces to undirected diffusion — exactly brute force, with no speedup.

This is not a limitation of a particular implementation. It is structural: Collaptics' advantage *is* the gradient, and a secure hash is the deliberate absence of one.

## The lesson

The honest boundary of the framework (see [`../theory/informational-collapse.md`](../theory/informational-collapse.md)) says Collaptics is an energy/throughput advantage on **smooth, crossable landscapes**, not a universal solver. Hash inversion is a clear case on the wrong side of that line. If Collaptics could invert SHA-256, the hash would already be broken by gradient descent — and it is not.

This negative case delineates the boundary of the framework as sharply as the positive examples.

---

See also: [`protein-folding.md`](protein-folding.md) · [`ai-inference.md`](ai-inference.md)
