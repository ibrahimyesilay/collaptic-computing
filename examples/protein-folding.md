# Example: Protein Folding

Protein folding is, at its core, an energy-minimization problem: a chain of amino acids settles into the three-dimensional structure of lowest free energy. That is the same shape as informational collapse, which makes it one of the more natural fits for Collaptics.

## The mapping

- The conformation of the protein is the configuration `x`.
- The molecule's free-energy surface is the informational potential `V(x)`.
- The native folded structure is the dominant minimum — a Collapse Singularity.

The protein is not *calculated*. It is *discovered* through collapse: encode the energy surface on the substrate, let the field flow downhill, and read the structure that the collapse settles into.

## Why the framing helps

Classical folding simulation spends enormous compute integrating equations of motion or searching conformations. Collaptics proposes letting a physical substrate do the minimization directly — the descent on `V` happens in hardware, in parallel, at the speed of the resonance dynamics, rather than being stepped through in software.

This is also where the abstract numbers become concrete: the resolving power `Σ = I·Ω²` sets how sharply the folded structure is pinned down, and the basin-pull `Γ` decides which fold wins when several are close in energy.

## Honest caveats

Folding landscapes are rugged. Two known difficulties apply directly:

- **Local minima.** A protein can be kinetically trapped in a misfolded state, exactly the `P5b` trapping behavior in [`../simulation/RESULTS.md`](../simulation/RESULTS.md). Collaptics finds the *reachable* minimum, not a guaranteed global one.
- **Barrier height.** Where folding requires crossing large barriers, time-to-collapse grows as `exp(βΔV)` — the same Arrhenius wall every method faces.

So Collaptics does not magically solve folding. It reframes it as a physical collapse and offers an energy/throughput advantage where the landscape is smooth enough to cross — which is also, encouragingly, the regime in which real proteins fold reliably.

---

See also: [`hash-inversion.md`](hash-inversion.md) · [`ai-inference.md`](ai-inference.md)
