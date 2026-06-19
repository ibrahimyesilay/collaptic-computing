# The Informational Field

*The medium of computation: a continuous probability field over candidate configurations.*

Where a classical machine holds a definite state, a Collaptics substrate holds a **field** — a probability density `P(x, t)` spread across the space of possible configurations `x`. A single Collapton is one local tendency; the informational field is the whole distributed cloud they form together. Computation is the evolution of this field, not the manipulation of symbols.

## Why a field, and not a collection of states

A field carries more than a set of candidate answers: it carries their relative weights, their correlations, and their uncertainty, all at once. The same way a gravitational or electromagnetic field assigns a value to every point in space, the informational field assigns a probability — a *tendency* — to every candidate configuration. The structure of the field at any instant is the machine's entire knowledge of the problem.

## How it evolves

The field follows the Fokker–Planck form of the Collapse Flow:

```
∂P/∂t = ∇·[ Ω²·(∇V)·P + D·∇P ]
```

Two forces act on it. The drift term `Ω²·(∇V)·P` pulls probability toward the minima of the potential `V` (toward solutions). The diffusion term `D·∇P` spreads it back out (exploration). Their balance is set by the inverse temperature `β = Ω²/D`. Early in a computation the field is broad and high-entropy; as coherence rises or noise falls, it sharpens. Full derivation: [`../mathematics/collapse-law.md`](../mathematics/collapse-law.md).

## Entropy and collapse

The field's Shannon entropy measures how undecided the machine still is. Informational collapse is precisely the monotone reduction of this entropy as the field concentrates onto a dominant configuration. The end state is the Gibbs field `P* ∝ exp(−βV)`, peaked at the Collapse Singularity.

## Physical reality of the field

The field is not a bookkeeping abstraction laid over a digital simulation. In a coherent substrate it is a literal physical object: the mode amplitudes of a coupled-oscillator network, the optical intensity pattern across a photonic mesh, or the spectral occupation of a resonant medium. Reading the field — by homodyne detection or intensity measurement — returns a sample from `P`. See [`../hardware/collaptic-substrate.md`](../hardware/collaptic-substrate.md).

---

Related: [`collapton.md`](collapton.md) · [`informational-collapse.md`](informational-collapse.md) · [`informational-gravity.md`](informational-gravity.md)
