# Reproducibility

Run `python scripts/render_public_assets.py --write`, then `python scripts/render_public_assets.py --check`, then `python scripts/verify_release.py`. The generators use only the Python standard library. The scope is artifact-level regeneration of reviewed aggregate tables and vector figure assets; raw municipal data are not bundled.
