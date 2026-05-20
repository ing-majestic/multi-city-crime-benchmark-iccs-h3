import pandas as pd


def test_baseline_schema():
    expected = {"city", "granularity", "model", "test_mae", "test_rmse", "test_r2", "audit_status"}
    for path in ["results/daily_baseline_results.csv", "results/monthly_baseline_results.csv"]:
        df = pd.read_csv(path)
        assert expected.issubset(df.columns)
        assert (df["audit_status"] == "ok").all()


def test_h3_panel_schema():
    df = pd.read_csv("metadata/benchmark_h3_panel_definition.csv")
    assert {"city", "granularity", "h3_unique_cells", "observed_h3_time_rows"}.issubset(df.columns)
    assert (df["observed_h3_time_rows"] > 0).all()
