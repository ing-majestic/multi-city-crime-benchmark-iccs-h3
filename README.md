# Multi-city administrative crime-count forecasting benchmark

This folder is a **release-candidate reconstruction** for the reviewed benchmark manuscript. It is not a published GitHub Release and has no DOI.

The benchmark predicts administrative `record_count` on complete predefined logical support. Eligible unit-period combinations without an observed administrative record are represented as structural zeros for this estimand; this does not assert that no real-world crime occurred.

Mexico City and Chicago daily families use local civic occurrence dates. London remains at native monthly resolution. Spatial support uses H3 resolution 9 with center containment as the selected boundary policy. Validation uses rolling-origin one-step-ahead prequential information updating with fold-static model parameters for validation years 2021, 2022 and 2023. The 2024 final-test period remains held out and is not used here.

Mandatory controls are zero, lag-1 persistence and seasonal naive. Evaluated learned comparators are Poisson GLM, NB2, Random Forest with Poisson criterion, and XGBoost with a count-Poisson objective. MAE is the primary metric and is interpreted within a benchmark family.

Raw municipal records and processed record-level derivatives are not redistributed. The package is bounded to deterministic artifact-level regeneration and verification from reviewed aggregate inputs.

Planned archival version: `v1.0.0`. No tag, GitHub Release, Zenodo archive, DOI, publication date, volume or issue is asserted by this candidate.
