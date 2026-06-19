# Example: Language Model Inference

Large language models are already probabilistic machines. Every step of generation produces a probability distribution over the next token; the model then samples from it. The distribution is the real object — the binary arithmetic underneath is just how today's hardware *simulates* it.

This is the most direct opening for Collaptics: represent the distribution in hardware instead of computing it with trillions of binary operations.

## The mapping

```
Question → Probability Topology → Collapse Singularity → Informational Collapse → Answer
```

- The prompt and model define an informational potential over possible continuations.
- The most likely continuation is the dominant attractor.
- Sampling a token is a collapse of the field onto one outcome.

## Why this is not a stretch

The framework's embedding theorem (see [`../mathematics/mathematical-foundations.md`](../mathematics/mathematical-foundations.md)) shows that **score-based diffusion models** are a corner of the Collapse Flow: their reverse-diffusion sampling *is* `dx = −Ω²∇V dt + √(2D)ξ` with `V = −(1/β)·log p`. Modern generative models already run a discretized, simulated version of Collaptics' core equation. A probabilistic substrate would run it natively.

The payoff is energy. The Collapse Law says resolving power scales as `Ω²` at fixed information and fixed energy landscape — a coherent substrate buys precision from physics that a digital machine has to pay for in operations.

## Where it fits, and where it does not

- **Good fit:** inference and sampling over smooth, learned landscapes — exactly what a trained model provides. Training shapes `V` to be navigable, which is precisely the regime Collaptics likes.
- **Not a fit:** tasks with flat or adversarial landscapes, or anything requiring guaranteed global optima. Collaptics samples and converges; it does not exhaustively search.

So the realistic claim is narrow and concrete: not "Collaptics replaces neural networks," but "the inference step of a probabilistic model is a physical collapse, and running it on a probabilistic substrate could make it dramatically cheaper."

---

See also: [`protein-folding.md`](protein-folding.md) · [`hash-inversion.md`](hash-inversion.md)
