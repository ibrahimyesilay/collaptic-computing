# The Photonic Interaction Layer

*Photons as carriers: low loss, and many degrees of freedom at once.*

An electron is usually used for one thing — its charge. A photon carries several independent quantities simultaneously: wavelength, phase, polarization, amplitude, spatial mode, and time of arrival. That is what lets a single waveguide hold what a wire cannot, and why the carrier layer of a Collaptics substrate is built from light.

## What this layer must do

Move and couple Collaptons with low loss, and provide enough degrees of freedom that many fields coexist. Three jobs: set the couplings `J_ij` of the problem, drive the resonance schedule `Ω(t)`, and read the settled field out.

## Building blocks

**Programmable coupling — silicon-photonic MZI meshes.** A mesh of Mach–Zehnder interferometers (Reck or Clements decomposition) implements an arbitrary linear transform in light. This is how the coupling matrix `J_ij` is written optically. Demonstrated for optical neural networks (Shen et al., 2017).

**Fast drive — thin-film lithium niobate (TFLN).** The Pockels effect gives electro-optic modulation above 100 GHz. This runs the anneal schedule and any fast field updates.

**Parallel channels — microrings + wavelength multiplexing (WDM).** Each wavelength is an independent channel, so many Collaptons ride different colours of light at once. This is the literal realization of "multiple information dimensions coexisting."

**Non-volatile optical weights — phase-change on waveguides.** Ge₂Sb₂Te₅ patches on a waveguide store a weight optically, merging memory and carrier in one device (photonic in-memory computing, Oxford/Münster).

**Massive parallelism — Kerr frequency combs.** A single pump in a Si₃N₄ microresonator produces hundreds of coherent comb lines — the carrier for a wide Collapton field.

## Reading the field

The phase and amplitude of the settled light are recovered by **homodyne / heterodyne detection** with balanced photodiodes. Phase gives the Collapton's `μ` and `φ` directly; repeated readouts give the variance, hence the resolving power `Σ`.

## Honest limit

Insertion loss accumulates through a deep mesh, which caps problem size and favors recurrent/iterative encodings over deep feed-forward ones. The analog-to-digital interface can also dominate energy if readouts are frequent — favor problems run to convergence in the optical domain with sparse digital I/O.

---

See also: [`resonance-dynamics-layer.md`](resonance-dynamics-layer.md) · [`collaptic-substrate.md`](collaptic-substrate.md)
