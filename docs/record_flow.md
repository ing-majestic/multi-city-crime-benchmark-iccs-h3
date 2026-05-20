# Record flow

The public record flow is summarized in `metadata/benchmark_record_flow.csv` and
`results/dataset_summary_table.csv`.

Cleaning rules exclude records with missing or invalid timestamps, coordinates,
or categories. Chicago and London use native unique identifiers for
deduplication. CDMX uses a synthetic fingerprint based on timestamp, latitude,
longitude, and crime category.
