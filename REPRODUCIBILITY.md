# Reproducibility

The public package supports deterministic regeneration and verification of the reviewed aggregate-derived tables and vector figures included in this repository. Raw municipal records are not bundled.

From the repository root:

```bash
python scripts/render_public_assets.py --write
python scripts/render_public_assets.py --check
sha256sum -c SHA256SUMS.txt
python scripts/verify_release.py
```

The renderer uses only the Python standard library. `--check` fails if a generated table or figure differs from deterministic regeneration. The SHA-256 command exits non-zero if any listed file differs from the recorded checksum. `verify_release.py` checks the scientific scope, data-availability boundaries, artifact registry, provenance files, source-rights metadata, checksum manifest, and generated outputs.

Stable public artifact identifiers are listed in `ARTIFACT_INDEX.json`. Source provenance is in `PROVENANCE.json` and official upstream source information is in `SOURCE_MANIFEST.json`.
