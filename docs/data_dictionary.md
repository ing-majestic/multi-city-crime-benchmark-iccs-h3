# Data dictionary

- `event_count`: raw incident count in an observed H3 cell-time window.
- `h3_cell`: Uber H3 cell identifier at resolution 9.
- `timestamp`: temporal aggregation window start.
- `city`: CDMX, Chicago, or London.
- `granularity`: daily or monthly.
- `model`: GLM, RF, or XGBoost.
- `test_mae`, `test_rmse`, `test_r2`: held-out benchmark metrics.
- `iccs_*`: fields derived from ICCS-compatible crime category mapping.

See `metadata/benchmark_feature_definitions.csv` for benchmark feature details.
