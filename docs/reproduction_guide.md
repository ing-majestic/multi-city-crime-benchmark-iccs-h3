# Reproduction guide

## Artifact-level reproduction

Use the included metadata, results, mappings, and figures to audit the benchmark
paper tables and figures without downloading raw data:

```bash
python scripts/00_check_environment.py
python scripts/06_generate_tables.py
python scripts/07_generate_figures.py
pytest
```

## Raw-data reproduction

Raw municipal datasets are not included. To rebuild from raw data, download the
sources described in `data_sources/download_instructions.md`, place them under
`data/raw/`, and run scripts `01` through `07` in order.

The benchmark uses a chronological 70/15/15 row-based split after timestamp
sorting, a H3 resolution 9 observed event panel, raw `event_count` as the target,
and GLM/RF/XGBoost baselines.
