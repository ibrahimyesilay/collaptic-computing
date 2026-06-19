# Example: Combinatorial Optimization

Combinatorial optimization is the most direct fit for Collaptics, because the hardware platforms that motivate the framework — coherent Ising machines, oscillator Ising machines, memristor crossbars — were built to solve exactly these problems. Collaptics is, in part, an attempt to describe what those machines are doing in a common language.

## The mapping

Many optimization problems can be written as the minimization of an Ising or quadratic energy:

```
V(s) = −½ · Σ_ij J_ij s_i s_j − Σ_i h_i s_i
```

The couplings `J_ij` and fields `h_i` encode the problem; the configuration `s` of lowest energy is the optimum. In Collaptics terms, `V` is the informational potential, its dominant minimum is the Collapse Singularity, and letting the substrate settle is informational collapse. The couplings are written into the persistent layer; the resonance layer relaxes toward the lowest-energy configuration.

## What Collaptics offers here

- **Energy efficiency.** The descent on `V` is performed by physics — gain competition among coupled oscillators — rather than by a processor stepping through candidate states. Where the landscape is navigable, this can reach a good configuration at far lower energy than a digital search.
- **Native parallelism.** All couplings act at once; the field explores many configurations simultaneously through diffusion.
- **Annealing for free.** Ramping the drive `Ω` (or lowering the noise `D`) is the physical analog of an annealing schedule, lowering `β` from exploration to commitment.

## What Collaptics does not offer

The limits of the approach are equally important.

- **No resolution of worst-case hardness.** For NP-hard problems, time-to-solution still grows as `exp(βΔV)` on the hard instances (test P6). Collaptics does not change complexity classes.
- **Approximate, not guaranteed optimal.** The field settles into the *reachable* attractor, which may be a local minimum (test P5b). The output is a high-quality candidate, not a certificate of optimality.
- **Landscape-dependent.** Problems whose energy surface is glassy or deceptive remain hard; the advantage appears on instances with structure a gradient can exploit.

The realistic claim is the same one the Ising-machine literature already supports: a physical, energy-efficient route to *good approximate solutions* on a useful class of optimization problems — not a universal optimizer.

---

See also: [`ai-inference.md`](ai-inference.md) · [`protein-folding.md`](protein-folding.md) · [`hash-inversion.md`](hash-inversion.md)
