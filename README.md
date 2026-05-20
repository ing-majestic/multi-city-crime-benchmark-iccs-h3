# Multi-city crime benchmark with ICCS and H3

This repository contains the public reproducibility package for a multi-city
crime prediction benchmark using ICCS-compatible semantic harmonization and H3
spatial indexing.

## Scope

Included:

- reproducibility metadata for the benchmark paper;
- ICCS mapping artifacts;
- final benchmark tables and publication figures;
- environment specifications;
- scripts that validate included artifacts and document the raw-data pipeline.

Not included:

- raw municipal crime datasets;
- large processed H3-time panels;
- temporary outputs, local paths, credentials, or personal files.

Raw source data must be downloaded from the official portals listed in
`data_sources/`.

## Reproducing included artifacts

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python scripts/00_check_environment.py
python scripts/06_generate_tables.py
python scripts/07_generate_figures.py
pytest
```

## Benchmark design

- Spatial index: Uber H3 resolution 9.
- Panel definition: observed event panel; zero-count cell-time pairs are not
  materialized.
- Target: raw `event_count`.
- Split: chronological 70% train, 15% validation, 15% test after timestamp
  sorting; no shuffling.
- Models: Poisson GLM, Random Forest, XGBoost with Poisson objective.

## Citation

Please cite the archived release using the metadata in `CITATION.cff`.

GitHub repository: https://github.com/ing-majestic/multi-city-crime-benchmark-iccs-h3

Once a Zenodo DOI is created, update this README and the manuscript availability
statement with the DOI URL.

## License

Code is released under the MIT License. Metadata, mappings, documentation, and
figures are released under CC BY 4.0 as described in `LICENSE-DATA-DOCS.md`.
Raw municipal datasets are not redistributed and remain subject to their
original source terms.
