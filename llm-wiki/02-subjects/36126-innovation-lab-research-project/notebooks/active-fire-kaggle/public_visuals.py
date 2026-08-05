import sys
import matplotlib
if "ipykernel" not in sys.modules:
    matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from typing import Dict, List

# Colorblind-friendly palette (Okabe-Ito)
OKABE_ITO_COLORS = ["#0072B2", "#E69F00", "#CC79A7", "#999999"]
SENSOR_COLORS = {
    "VIIRS": "#0072B2",
    "MODIS": "#E69F00",
    "AHI": "#CC79A7",
    "unmatched": "#999999",
    "unresolved": "#999999"
}

def _apply_premium_style(ax: plt.Axes, title: str, xlabel: str = "", ylabel: str = ""):
    """Applies clean, publication-quality theme settings to Matplotlib axes."""
    ax.set_facecolor("white")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#333333")
    ax.spines["bottom"].set_color("#333333")
    ax.spines["left"].set_linewidth(1.0)
    ax.spines["bottom"].set_linewidth(1.0)
    
    ax.tick_params(colors="#333333", labelsize=9, width=1.0)
    if title:
        ax.set_title(title, color="black", fontsize=11, fontweight="bold", pad=16, loc="left")
    if xlabel:
        ax.set_xlabel(xlabel, color="#333333", fontsize=9.5, labelpad=8)
    if ylabel:
        ax.set_ylabel(ylabel, color="#333333", fontsize=9.5, labelpad=8)


def plot_sensor_composition(frame: pd.DataFrame) -> plt.Figure:
    """Plot the total count of hotspots by sensor."""
    fig, ax = plt.subplots(figsize=(6.5, 4.0), facecolor="white")
    
    df = frame.sort_values(by="total_hotspots", ascending=True)
    total_n = df["total_hotspots"].sum()
    
    # Map colors to sensors
    colors = [SENSOR_COLORS.get(sensor, OKABE_ITO_COLORS[0]) for sensor in df["sensor"]]
    
    bars = ax.barh(df["sensor"], df["total_hotspots"], color=colors, height=0.55)
    _apply_premium_style(ax, f"Active-Fire Hotspots by Sensor (Total N={total_n:,})", "Total Hotspot Observations")
    
    # Grid lines only vertical, very light
    ax.grid(True, axis="x", linestyle=":", alpha=0.4, color="#CCCCCC", zorder=0)
    ax.set_axisbelow(True)
    
    # Value labels
    for bar in bars:
        width = bar.get_width()
        pct = (width / total_n) * 100.0
        ax.text(width + (total_n * 0.01), bar.get_y() + bar.get_height()/2, 
                f"{int(width):,} ({pct:.1f}%)", 
                va="center", ha="left", color="black", fontsize=8.5, fontweight="semibold")
                
    # Extra right padding
    ax.set_xlim(0, max(df["total_hotspots"]) * 1.15)
    fig.tight_layout()
    return fig


def plot_match_rates(frame: pd.DataFrame) -> plt.Figure:
    """Plot match rate by sensor with denominators in the labels."""
    fig, ax = plt.subplots(figsize=(7.0, 4.0), facecolor="white")
    
    labels = []
    rates = []
    colors = []
    for _, row in frame.iterrows():
        sensor = row["sensor"]
        n = int(row["total_hotspots"])
        rate = float(row["match_rate"])
        labels.append(f"{sensor}\n(n={n:,})")
        rates.append(rate * 100.0)
        colors.append(SENSOR_COLORS.get(sensor, OKABE_ITO_COLORS[1]))
        
    y_pos = np.arange(len(labels))
    bars = ax.barh(y_pos, rates, color=colors, height=0.55)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels, color="black", fontsize=9)
    
    _apply_premium_style(ax, "Spatiotemporal Match Rate by Sensor", "Match Rate (%)")
    
    ax.grid(True, axis="x", linestyle=":", alpha=0.4, color="#CCCCCC", zorder=0)
    ax.set_axisbelow(True)
    ax.set_xlim(0, 108)
    
    # Labels on bars
    for bar in bars:
        width = bar.get_width()
        ax.text(width + 1.8, bar.get_y() + bar.get_height()/2, f"{width:.2f}%", 
                va="center", ha="left", color="black", fontsize=8.5, fontweight="semibold")
                
    fig.tight_layout()
    return fig


def plot_confidence_by_algorithm(frame: pd.DataFrame) -> plt.Figure:
    """Plot confidence distributions by sensor / algorithm."""
    fig, ax = plt.subplots(figsize=(7.0, 4.5), facecolor="white")
    
    sensors = sorted(frame["sensor"].dropna().unique())
    data = []
    labels = []
    for sensor in sensors:
        subset = frame[frame["sensor"] == sensor]["confidence"].dropna()
        if not subset.empty:
            data.append(subset.values)
            labels.append(f"{sensor}\n(n={len(subset):,})")
            
    if data:
        # Custom boxplot styling
        try:
            import re
            v_parts = [int(x) for x in re.findall(r"\d+", matplotlib.__version__)]
        except Exception:
            v_parts = [3, 0]
        use_tick_labels = len(v_parts) >= 2 and (v_parts[0] > 3 or (v_parts[0] == 3 and v_parts[1] >= 9))
        
        flierprops = dict(marker="o", markersize=3.0, markerfacecolor="#999999", markeredgecolor="none", alpha=0.3)
        boxprops = dict(linewidth=1.2, edgecolor="#222222")
        whiskerprops = dict(linewidth=1.0, color="#666666", linestyle="-")
        capprops = dict(linewidth=1.0, color="#666666")
        medianprops = dict(linewidth=1.5, color="black")
        
        if use_tick_labels:
            box = ax.boxplot(data, tick_labels=labels, patch_artist=True, widths=0.45,
                             flierprops=flierprops, boxprops=boxprops, whiskerprops=whiskerprops,
                             capprops=capprops, medianprops=medianprops)
        else:
            box = ax.boxplot(data, labels=labels, patch_artist=True, widths=0.45,
                             flierprops=flierprops, boxprops=boxprops, whiskerprops=whiskerprops,
                             capprops=capprops, medianprops=medianprops)
            
        # Color each box corresponding to its sensor
        for idx, patch in enumerate(box["boxes"]):
            sensor_name = sensors[idx]
            patch.set_facecolor(SENSOR_COLORS.get(sensor_name, OKABE_ITO_COLORS[idx % len(OKABE_ITO_COLORS)]))
            patch.set_alpha(0.85)
            
    _apply_premium_style(ax, "Confidence Score Distribution by Sensor", ylabel="Confidence score / value")
    ax.grid(True, axis="y", linestyle=":", alpha=0.4, color="#CCCCCC", zorder=0)
    ax.set_axisbelow(True)
    
    fig.tight_layout()
    return fig


def plot_event_concentration(frame: pd.DataFrame) -> plt.Figure:
    """Plot hotspot count by fire event to show spatial concentration."""
    fig, ax = plt.subplots(figsize=(7.0, 4.5), facecolor="white")
    
    top_events = frame.head(10).copy()
    total_matched = frame["matched_hotspots"].sum()
    
    labels = []
    for _, row in top_events.iterrows():
        name = str(row["fire_name"])
        if len(name) > 20:
            name = name[:18] + "..."
        labels.append(name)
        
    y_pos = np.arange(len(labels))
    bars = ax.barh(y_pos, top_events["matched_hotspots"], color=OKABE_ITO_COLORS[0], edgecolor="none", height=0.55)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels, color="black", fontsize=9)
    ax.invert_yaxis()
    
    _apply_premium_style(ax, f"Match Concentration Across Top 10 Events (Total Matched N={total_matched:,})", "Number of Matched Hotspots")
    
    ax.grid(True, axis="x", linestyle=":", alpha=0.4, color="#CCCCCC", zorder=0)
    ax.set_axisbelow(True)
    
    # Value labels
    for bar in bars:
        width = bar.get_width()
        pct = (width / total_matched) * 100.0
        ax.text(width + (total_matched * 0.01), bar.get_y() + bar.get_height()/2, 
                f"{int(width):,} ({pct:.1f}%)", 
                va="center", ha="left", color="black", fontsize=8.5, fontweight="semibold")
                
    ax.set_xlim(0, max(top_events["matched_hotspots"]) * 1.15)
    fig.tight_layout()
    return fig


def plot_pilot_map(hotspots: pd.DataFrame, polygons: List[dict], displayed_n: int) -> plt.Figure:
    """Plot map showing hotspots and fire event boundary polygons."""
    fig, ax = plt.subplots(figsize=(8.0, 7.5), facecolor="white")
    
    # 1. Plot polygons
    for feature in polygons:
        geometry = feature.get("geometry", {})
        coords = geometry.get("coordinates", [])
        geom_type = geometry.get("type")
        
        poly_list = [coords] if geom_type == "Polygon" else coords
        for poly in poly_list:
            for ring in poly:
                x = [pt[0] for pt in ring]
                y = [pt[1] for pt in ring]
                ax.plot(x, y, color="black", linewidth=1.0, alpha=0.5, zorder=2)
                ax.fill(x, y, color="#999999", alpha=0.1, zorder=1)
                
    # 2. Plot hotspots colored by sensor mapping (with distinct markers)
    matched = hotspots[hotspots["match_class"].isin(["bushfire", "prescribed_burn", "other_fire", "spatial_only"])]
    unmatched = hotspots[hotspots["match_class"] == "unmatched"]
    
    # Plot matched by sensor type
    sensors = sorted(matched["sensor"].dropna().unique())
    for sensor in sensors:
        subset = matched[matched["sensor"] == sensor]
        ax.scatter(subset["longitude"], subset["latitude"], 
                   color=SENSOR_COLORS.get(sensor, OKABE_ITO_COLORS[1]), 
                   label=f"Matched {sensor} (n={len(subset):,})", 
                   s=12, alpha=0.65, zorder=4, marker="o", edgecolors="none")
                   
    # Plot unmatched (unresolved)
    ax.scatter(unmatched["longitude"], unmatched["latitude"], 
               color=SENSOR_COLORS["unresolved"], 
               label=f"Unresolved (n={len(unmatched):,})", 
               s=8, alpha=0.45, zorder=3, marker="x")
               
    _apply_premium_style(ax, f"Active-Fire Spatiotemporal Match Map (Sample Size: {displayed_n:,})", 
                         "Longitude (WGS84)", "Latitude (WGS84)")
    
    # Zoom bounds tightly around the hotspot coordinate bounds with clean margins
    ax.set_xlim(149.3, 151.3)
    ax.set_ylim(-33.8, -31.2)
    
    ax.legend(facecolor="white", edgecolor="#CCCCCC", labelcolor="black", loc="upper right", framealpha=0.9, fontsize=8.5)
    ax.grid(True, linestyle=":", alpha=0.4, color="#CCCCCC", zorder=0)
    
    fig.tight_layout()
    return fig
