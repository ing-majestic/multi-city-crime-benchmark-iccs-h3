from pathlib import Path


EXPECTED = [
    "README.md",
    "CITATION.cff",
    "DATA_AVAILABILITY.md",
    "ARTIFACTS.md",
    "metadata/benchmark_temporal_splits.csv",
    "metadata/benchmark_h3_panel_definition.csv",
    "metadata/benchmark_target_model_specification.csv",
    "results/monthly_baseline_results.csv",
    "results/figures/fig04_daily_vs_monthly_best_r2.png",
]


def test_expected_files_exist():
    for rel in EXPECTED:
        assert Path(rel).exists(), rel
