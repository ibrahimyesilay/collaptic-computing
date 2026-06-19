# Publication Checklist

A checklist for releasing and archiving Collaptics v1.0. Markdown is the canonical format throughout — there are no binary PDF artifacts to maintain, which keeps the record diff-able and readable far into the future.

## Repository content

- [x] `README.md` with abstract, key concepts, structure, honest boundaries, status, citation, license, author
- [x] `LICENSE` (CC BY-NC 4.0)
- [x] `CITATION.cff` (machine-readable citation metadata)
- [x] `.zenodo.json` (archival metadata)
- [x] `CONTRIBUTING.md`
- [x] `CODE_OF_CONDUCT.md`
- [x] `whitepaper/` — English (authoritative) and Turkish editions
- [x] `theory/` — core concept pages
- [x] `mathematics/` — collapse law, probability topology, information geometry, foundations
- [x] `hardware/` — substrate layers and speculative materials
- [x] `examples/` — including an honest negative result
- [x] `simulation/` — runnable, deterministic numerical checks
- [x] `tr/` — Turkish edition

## Integrity and tone

- [x] No claim of experimental validation, physical prototype, or new physics
- [x] Prominent disclaimer in the README
- [x] Dedicated "Honest Boundaries" section
- [x] Every strong claim anchored to established results or marked speculative
- [x] Sensational phrasing removed (no "guaranteed," "revolutionary," "replaces quantum," "solves cryptography")
- [x] Simulation predictions stated with the formula each one checks

## Before pushing to GitHub (done by the author)

- [ ] Create the repository under the intended account/organization
- [ ] Verify `git log` shows the intended author identity and a clean message
- [ ] Confirm no secrets, tokens, or credentials are present anywhere in the history
- [ ] Push, then tag the release `v1.0.0`
- [ ] Draft a GitHub Release titled "Collaptics v1.0 — Initial Public Release" using `release-notes-v1.0.md`

## Archival on Zenodo (done by the author)

- [ ] Follow [`zenodo-guide.md`](zenodo-guide.md)
- [ ] Confirm `.zenodo.json` metadata is picked up
- [ ] Obtain the DOI and add it to `CITATION.cff` and the README citation block
- [ ] Verify the deposited record is open access under CC BY-NC 4.0

## Security

- [ ] No access tokens committed to the repository or pasted into any file
- [ ] Any token previously exposed in chat or logs has been revoked and regenerated
