# Reproducibility

Run the following from the repository root, in this order:

```bash
sha256sum -c SHA256SUMS.txt
python scripts/render_public_assets.py --write
python scripts/render_public_assets.py --check
python scripts/verify_release.py
```

`sha256sum -c SHA256SUMS.txt` is the cryptographic integrity gate for the allowlisted release-candidate files and exits non-zero if any listed file does not match its recorded SHA-256 digest.

The generators use only the Python standard library. The scope is artifact-level regeneration of reviewed aggregate tables and vector figure assets; raw municipal data and processed record-level derivatives are not bundled. Source-specific rights, attribution requirements, and non-redistribution boundaries are documented in `LICENSE_AND_RIGHTS_AUDIT.md`, `LICENSE-DATA-DOCS.md`, and `data_acquisition/SOURCE_ACQUISITION_MANIFEST.json`.
