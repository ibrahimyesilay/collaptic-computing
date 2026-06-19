# Archiving Collaptics on Zenodo

This guide explains how to deposit the repository on [Zenodo](https://zenodo.org) to obtain a permanent DOI. Everything here is performed **by the author**, in their own environment. No credentials are stored in this repository.

> **Security first.** A Zenodo personal access token grants write access to your account. Never paste it into a file, a commit, a chat, or a log. If a token is ever exposed, revoke it immediately at *Zenodo → Applications → Personal access tokens* and generate a new one. Tokens belong only in environment variables on your own machine.

## Recommended route: GitHub–Zenodo integration

This is the simplest and safest method — no token handling at all.

1. Sign in to Zenodo with GitHub.
2. Go to *Zenodo → Account → GitHub* and toggle the repository **on**.
3. On GitHub, create a release and tag it `v1.0.0` (title: "Collaptics v1.0 — Initial Public Release").
4. Zenodo automatically archives that release and mints a DOI.
5. Zenodo reads the metadata in [`../.zenodo.json`](../.zenodo.json) and the citation in [`../CITATION.cff`](../CITATION.cff).
6. Copy the DOI back into `CITATION.cff` (the commented `identifiers` block) and the README citation.

Zenodo issues two DOIs: a **concept DOI** (always points to the latest version) and a **version DOI** (this exact release). Cite the version DOI for reproducibility; link the concept DOI for "all versions."

## Alternative route: REST API (manual upload)

Use this only if you are not archiving via a GitHub release. Keep the token in an environment variable; do not write it into any file.

```bash
# Set the token in your shell session only (never commit it):
export ZENODO_TOKEN="<your-personal-access-token>"

# 1) Create a new deposition
DEP=$(curl -s -X POST "https://zenodo.org/api/deposit/depositions" \
  -H "Authorization: Bearer $ZENODO_TOKEN" \
  -H "Content-Type: application/json" -d '{}')
BUCKET=$(echo "$DEP" | python3 -c "import sys,json;print(json.load(sys.stdin)['links']['bucket'])")
ID=$(echo "$DEP" | python3 -c "import sys,json;print(json.load(sys.stdin)['id'])")

# 2) Upload a zipped snapshot of the repository
zip -r collaptic-computing-v1.0.0.zip . -x '.git/*'
curl -s -X PUT "$BUCKET/collaptic-computing-v1.0.0.zip" \
  -H "Authorization: Bearer $ZENODO_TOKEN" --upload-file collaptic-computing-v1.0.0.zip > /dev/null

# 3) Attach metadata (.zenodo.json) and publish from the Zenodo web UI after review.
```

Review the draft in the Zenodo web interface before publishing. **Publishing is irreversible** — the record and its files become permanent.

## Suggested metadata

Already provided in [`../.zenodo.json`](../.zenodo.json):

- **Title:** Collaptic Computing: A Post-Binary Computational Paradigm Based on Probability Fields, Photonic Resonance, and Informational Collapse
- **Author:** Yesilay, Ibrahim
- **Upload type:** Publication → Working paper
- **License:** CC BY-NC 4.0
- **Version:** 1.0.0
- **Keywords:** collaptic computing, post-binary computing, probability fields, informational collapse, photonic computing, unconventional computing, computer architecture, information theory, analog computing

## After archiving

- Add the version DOI to `CITATION.cff` and the README.
- Add a DOI badge to the README if desired:
  `[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)`
