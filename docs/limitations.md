# Limitations

- The benchmark panel is an observed event panel. Zero-count H3 cell-time pairs
  are not materialized in the released benchmark tables.
- London is excluded from daily benchmark comparisons because the source data
  used in the pipeline does not provide the same daily granularity required for
  the cross-city benchmark.
- Absolute error metrics should not be interpreted as directly comparable across
  cities or granularities because event density and aggregation scale differ.
- The repository does not redistribute raw municipal datasets; users must obtain
  them from the original public portals.
