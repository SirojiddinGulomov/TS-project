"""Utility functions for the final time-series course project."""

from __future__ import annotations
import numpy as np
import pandas as pd

DATA_URL = (
    "https://raw.githubusercontent.com/pplonski/datasets-for-start/"
    "refs/heads/master/aep-hourly-energy-consumption/AEP_hourly.csv"
)

def load_and_prepare(url: str = DATA_URL, fast_mode: bool = True) -> pd.DataFrame:
    """Load AEP data and convert it to Nixtla format."""
    raw = pd.read_csv(url)
    raw["Datetime"] = pd.to_datetime(raw["Datetime"], errors="coerce")
    raw = raw.dropna(subset=["Datetime", "AEP_MW"]).sort_values("Datetime")
    raw = raw.drop_duplicates(subset=["Datetime"], keep="last")
    raw = raw.set_index("Datetime").asfreq("h")
    raw["AEP_MW"] = raw["AEP_MW"].interpolate(limit=3).ffill().bfill()

    if fast_mode:
        # A one-year slice is enough to preserve daily/weekly seasonality
        # while keeping Colab runtime reasonable.
        raw = raw.tail(24 * 365)

    df = raw.reset_index().rename(columns={"Datetime": "ds", "AEP_MW": "y"})
    df["unique_id"] = "AEP"
    return df[["unique_id", "ds", "y"]]

def train_test_split_ts(df: pd.DataFrame, horizon: int = 24):
    return df.iloc[:-horizon].copy(), df.iloc[-horizon:].copy()

def metrics(y_true, y_pred) -> dict:
    y_true = np.asarray(y_true, dtype=float)
    y_pred = np.asarray(y_pred, dtype=float)
    err = y_true - y_pred
    mae = np.mean(np.abs(err))
    rmse = np.sqrt(np.mean(err ** 2))
    denom = np.maximum(np.abs(y_true), 1e-8)
    mape = np.mean(np.abs(err) / denom) * 100
    smape = np.mean(
        2 * np.abs(err) / np.maximum(np.abs(y_true) + np.abs(y_pred), 1e-8)
    ) * 100
    return {"MAE": mae, "RMSE": rmse, "MAPE": mape, "sMAPE": smape}
