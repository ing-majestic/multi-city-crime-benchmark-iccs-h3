"""Validate included benchmark result tables."""

from pathlib import Path
import pandas as pd

REQUIRED = [
    "results/daily_baseline_results.csv",
    "results/monthly_baseline_results.csv",
    "results/dataset_summary_table.csv",
    "results/iccs_mapping_coverage_table.csv",
    "metadata/benchmark_temporal_splits.csv",
    "metadata/benchmark_h3_panel_definition.csv",
]


def main() -> int:
    for rel in REQUIRED:
        path = Path(rel)
        if not path.exists():
            print(f"Missing {rel}")
            return 1
        df = pd.read_csv(path)
        print(f"OK {rel}: {len(df)} rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
