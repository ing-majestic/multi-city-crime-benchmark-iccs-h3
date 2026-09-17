# Multi-city administrative crime-count forecasting benchmark

This repository contains the public reproducibility package associated with the benchmark study **An Evidence-Traceable Multi-City Benchmark for Spatio-Temporal Administrative Crime Count Forecasting**.

The benchmark predicts administrative `record_count` on complete predefined logical support. Eligible unit-period combinations without an observed administrative record are represented as structural zeros for this estimand; this does not assert that no real-world crime occurred.

Mexico City and Chicago daily families use local civic occurrence dates. London remains at native monthly resolution. Spatial support uses H3 resolution 9 with center containment as the selected boundary policy. Validation uses rolling-origin one-step-ahead prequential information updating with fold-static model parameters for validation years 2021, 2022 and 2023. The 2024 final-test period remains held out and is not used here.

Mandatory controls are zero, lag-1 persistence and seasonal naive. Evaluated learned comparators are Poisson GLM, NB2, Random Forest with Poisson criterion, and XGBoost with a count-Poisson objective. MAE is the primary metric and is interpreted within a benchmark family.

## Public artifact identifiers

`ARTIFACT_INDEX.json` assigns stable public identifiers to the principal datasets, tables, figures, provenance records, reproducibility tools and rights records used by the study. Identifiers follow the form `ART01-<CLASS>-<NNN>` and are designed to remain stable across the publication package.

These identifiers support direct manuscript-to-repository traceability. For example, `ART01-TBL-002` identifies the benchmark performance table and links it to its machine-readable source and public provenance record.

## Reproducibility scope

Raw municipal records and processed record-level derivatives are not redistributed. The package supports deterministic artifact-level regeneration and verification from reviewed aggregate inputs. See `REPRODUCIBILITY.md` for the exact verification commands, `PROVENANCE.json` for artifact lineage, `SOURCE_MANIFEST.json` for official upstream sources, and `SHA256SUMS.txt` for cryptographic integrity checks.

## Rights and source attribution

Software is covered by the root MIT `LICENSE`. Repository-authored documentation and figures, together with the scoped treatment of aggregate outputs, are described in `LICENSE-DATA-DOCS.md`. Source-specific terms, attribution requirements and exclusions are summarized in `RIGHTS_AND_LICENSES.md` and `SOURCE_MANIFEST.json`. Repository licenses do not relicense third-party source data or UNODC ICCS content.

## Package status

The reproducibility package is prepared for an immutable archival release. A release tag, Zenodo archive and DOI have not yet been assigned. When an archival DOI exists, the repository and manuscript availability statement can be updated with that immutable identifier without changing the scientific results.
