# Multi-city administrative crime-count forecasting benchmark

This branch stages the reproducibility package for the reviewed manuscript **“An Evidence-Traceable Multi-City Benchmark for Spatio-Temporal Administrative Crime Count Forecasting.”** It is not yet a published release.

## Scientific scope

The benchmark predicts administrative `record_count` on complete predefined logical support. Eligible unit-period combinations without an observed administrative record are represented as structural zeros for this estimand; a zero does not assert that no real-world crime occurred.

Mexico City and Chicago daily families use local civic occurrence dates. London remains at native monthly resolution. Spatial support uses H3 resolution 9 with center containment as the selected boundary policy. Validation uses rolling-origin one-step-ahead prequential information updating with fold-static model parameters for validation years 2021, 2022, and 2023. The 2024 final-test period remains held out and is not used in this package.

Mandatory controls are zero, lag-1 persistence, and seasonal naive. Evaluated learned comparators are Poisson GLM, NB2, Random Forest with Poisson criterion, and XGBoost with a count-Poisson objective. Mean Absolute Error (MAE) is the primary metric and is interpreted within a benchmark family.

## Reproducibility scope

This repository supports deterministic artifact-level regeneration and verification of reviewed aggregate tables and figure assets from versioned machine-readable inputs. It does not claim end-to-end raw-data reproduction from redistributed municipal records. Raw municipal data and processed record-level derivatives are not bundled.

Run:

```bash
python scripts/render_public_assets.py --check
python scripts/verify_release.py
```

## Release status

Planned release: `v1.0.0`.

No GitHub Release, tag, Zenodo archive, DOI, publication date, volume, or issue is asserted by this staging branch. Publication remains blocked until an independent package audit passes and owner-authorized citation metadata is complete.

A final `CITATION.cff` is intentionally not emitted because archival author order and corresponding-author metadata have not been owner-confirmed. See `citation/CITATION_PREPARATION.json`.

See `DATA_RELEASE_DECISION.json` and `LICENSE_AND_RIGHTS_AUDIT.md`. The default is no redistribution of raw municipal datasets.
