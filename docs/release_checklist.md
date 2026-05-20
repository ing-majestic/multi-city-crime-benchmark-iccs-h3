# Release checklist

- [ ] Confirm no raw municipal datasets are present.
- [ ] Confirm no large H3-time panels are present.
- [ ] Confirm no local paths, credentials, temporary outputs, or personal files.
- [ ] Run `python scripts/00_check_environment.py`.
- [ ] Run `python scripts/06_generate_tables.py`.
- [ ] Run `python scripts/07_generate_figures.py`.
- [ ] Run `pytest`.
- [ ] Validate table counts against `metadata/benchmark_record_flow.csv`.
- [ ] Create GitHub repository.
- [ ] Create release `v1.0.0`.
- [ ] Archive the release on Zenodo.
- [ ] Update the manuscript Data and Code Availability section with the DOI.
