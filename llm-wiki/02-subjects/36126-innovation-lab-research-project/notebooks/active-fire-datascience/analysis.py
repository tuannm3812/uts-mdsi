"""Deterministic analysis functions for the exploratory EDA + feature-engineering
notebook. Kept separate from notebook cell text (mirrors the convention in
notebooks/active-fire-kaggle/public_analysis.py) so logic is unit-testable and
narrative text can be generated from real computed values, not hand-typed.
"""

from __future__ import annotations

import json
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any

import pandas as pd


def load_hotspots(path: Path) -> pd.DataFrame:
    document = json.loads(path.read_text())
    rows = []
    for feature in document["features"]:
        props = feature["properties"]
        lon, lat = feature["geometry"]["coordinates"][:2]
        rows.append({**props, "lon": lon, "lat": lat})
    df = pd.DataFrame(rows)
    df["datetime"] = pd.to_datetime(df["datetime"], utc=True, errors="coerce")
    df["date"] = df["datetime"].dt.date
    return df


def load_weather(data_dir: Path, point_names: list[str]) -> dict[str, pd.DataFrame]:
    weather = {}
    for name in point_names:
        path = data_dir / f"silo_weather_{name}.csv"
        df = pd.read_csv(path, skipinitialspace=True)
        df.columns = [c.strip() for c in df.columns]
        df["date"] = pd.to_datetime(df["YYYY-MM-DD"]).dt.date
        weather[name] = df
    return weather


def load_landcover(path: Path) -> pd.DataFrame:
    records = json.loads(path.read_text())
    return pd.DataFrame(records)


def daily_hotspot_counts(hotspots: pd.DataFrame) -> pd.DataFrame:
    counts = hotspots.groupby("date").size().rename("hotspot_count").reset_index()
    return counts.sort_values("date")


def sensor_composition(hotspots: pd.DataFrame) -> dict[str, int]:
    return dict(Counter(hotspots["sensor"].fillna("unknown")))


def confidence_summary(hotspots: pd.DataFrame) -> pd.DataFrame:
    """Confidence is numeric for MODIS/AHI but a coarse nominal/high scale for
    VIIRS in this project's earlier findings (T-025) -- report per-sensor
    stats rather than one pooled number, which would be misleading."""
    numeric_confidence = pd.to_numeric(hotspots["confidence"], errors="coerce")
    summary = hotspots.assign(confidence_numeric=numeric_confidence).groupby("sensor")[
        "confidence_numeric"
    ].agg(["count", "mean", "median", "min", "max", "nunique"])
    return summary


def rolling_dryness_features(weather_df: pd.DataFrame) -> pd.DataFrame:
    """Candidate weather features for the eventual forecasting model: rolling
    cumulative rainfall, consecutive dry days, and max-temp trend."""
    df = weather_df.sort_values("date").copy()
    df["rain_7d_sum"] = df["daily_rain"].rolling(7, min_periods=1).sum()
    df["rain_14d_sum"] = df["daily_rain"].rolling(14, min_periods=1).sum()
    df["is_dry_day"] = df["daily_rain"] < 1.0
    df["consecutive_dry_days"] = (
        df["is_dry_day"].groupby((~df["is_dry_day"]).cumsum()).cumcount() + 1
    ) * df["is_dry_day"]
    df["max_temp_7d_mean"] = df["max_temp"].rolling(7, min_periods=1).mean()
    df["vpd_7d_mean"] = df["vp_deficit"].rolling(7, min_periods=1).mean()
    return df


def merge_hotspots_weather(daily_counts: pd.DataFrame, weather_df: pd.DataFrame) -> pd.DataFrame:
    merged = daily_counts.merge(weather_df, on="date", how="outer").sort_values("date")
    merged["hotspot_count"] = merged["hotspot_count"].fillna(0)
    return merged


def landcover_class_distribution(landcover: pd.DataFrame) -> pd.Series:
    return landcover["level3_label"].value_counts()
