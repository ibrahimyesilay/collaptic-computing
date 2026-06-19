# Contributing to Collaptic Computing

Thank you for your interest. Collaptics is an open theoretical research framework, and thoughtful contributions are welcome — especially critical ones.

## What this project values

Collaptics advances by being **challenged**, not promoted. The most valuable contributions are those that test the framework's claims and mark its limits clearly.

Particularly welcome:

- **Falsification attempts.** The framework states explicit, testable predictions (see [`mathematics/mathematical-foundations.md`](mathematics/mathematical-foundations.md) and [`simulation/`](simulation/)). Numerical or analytical work that confirms, sharpens, or *breaks* them is the highest-value contribution.
- **Boundary-finding.** New cases where Collaptics offers no advantage, analogous to [`examples/hash-inversion.md`](examples/hash-inversion.md).
- **Connections to established theory.** Pointers showing that a Collaptics concept is a special case of, equivalent to, or contradicted by existing results in stochastic dynamics, information geometry, statistical mechanics, or device physics.
- **Corrections.** Mathematical errors, mis-citations, or overstated claims.
- **Translations and clarity.** Making the material accessible to more readers.

## Principles

1. **Intellectual honesty over advocacy.** Do not add claims of experimental validation, physical implementation, or new physics. If a statement cannot be supported, qualify it or remove it.
2. **Every strong claim is anchored or flagged.** Tie new claims to an established result, or mark them explicitly as speculation.
3. **Keep the boundaries visible.** Contributions that would blur the line between "demonstrated," "self-consistent," and "speculative" will be asked to restore it.

## How to contribute

1. Open an issue describing the change, the claim, or the test.
2. For text, keep the existing tone: serious, clear, and unsensational.
3. For simulation code, keep it dependency-light (numpy) and deterministic (fixed seeds), and state the formula each test checks.
4. Submit a pull request referencing the issue.

## Scope

This repository is an archival record of a theoretical framework. It is not a product, and there is no roadmap obligation. Contributions are accepted on the basis of correctness, clarity, and honesty.

## License

By contributing, you agree that your contributions are licensed under [CC BY-NC 4.0](LICENSE), consistent with the rest of the repository. You also grant the author permission to license your contributions commercially as part of the work.
