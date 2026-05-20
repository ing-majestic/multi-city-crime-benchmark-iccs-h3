"""Validate included publication figures."""

from pathlib import Path

REQUIRED = [
    "results/figures/fig01_reproducible_pipeline.png",
    "results/figures/fig02_retention_quality_by_city.png",
    "results/figures/fig03_iccs_mapping_coverage.png",
    "results/figures/fig04_daily_vs_monthly_best_r2.png",
]


def main() -> int:
    for rel in REQUIRED:
        path = Path(rel)
        if not path.exists() or path.stat().st_size == 0:
            print(f"Missing or empty {rel}")
            return 1
        print(f"OK {rel}: {path.stat().st_size} bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
