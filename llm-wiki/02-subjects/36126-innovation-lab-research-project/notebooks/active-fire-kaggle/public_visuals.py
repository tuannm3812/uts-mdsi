import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from typing import Dict, List

OKABE_ITO_COLORS = ["#0072B2", "#E69F00", "#CC79A7", "#999999"]


def plot_sensor_composition(frame: pd.DataFrame) -> plt.Figure:
    """Plot the total count of hotspots by sensor."""
    fig, ax = plt.subplots(figsize=(6, 4.5), facecolor="white")
    ax.set_facecolor("white")
    
    # Sort for consistent display
    df = frame.sort_values(by="total_hotspots", ascending=True)
    total_n = df["total_hotspots"].sum()
    
    bars = ax.barh(df["sensor"], df["total_hotspots"], color=OKABE_ITO_COLORS[0], edgecolor="none")
    ax.set_xlabel("Total Hotspot Observations", color="black", fontsize=10)
    ax.set_title(f"Hotspot Observations by Sensor (Total N={total_n:,})", color="black", fontsize=12, pad=15)
    
    # Style axes
    ax.tick_params(colors="black", labelsize=9)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("black")
    ax.spines["bottom"].set_color("black")
    
    for bar in bars:
        width = bar.get_width()
        ax.text(width + (width * 0.01) + 1, bar.get_y() + bar.get_height()/2, f"{int(width):,}", 
                va="center", ha="left", color="black", fontsize=9)
                
    fig.tight_layout()
    return fig


def plot_match_rates(frame: pd.DataFrame) -> plt.Figure:
    """Plot match rate by sensor with denominators in the labels."""
    fig, ax = plt.subplots(figsize=(7, 4.5), facecolor="white")
    ax.set_facecolor("white")
    
    # Create labels with denominators
    labels = []
    rates = []
    for _, row in frame.iterrows():
        sensor = row["sensor"]
        n = int(row["total_hotspots"])
        rate = float(row["match_rate"])
        labels.append(f"{sensor}\n(n={n:,})")
        rates.append(rate * 100.0)  # Percentage
        
    y_pos = np.arange(len(labels))
    bars = ax.barh(y_pos, rates, color=OKABE_ITO_COLORS[1], edgecolor="none")
    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels, color="black", fontsize=9)
    ax.set_xlabel("Spatiotemporal Match Rate (%)", color="black", fontsize=10)
    ax.set_title("Active-Fire Match Rate by Sensor", color="black", fontsize=12, pad=15)
    ax.set_xlim(0, 105)
    
    # Style axes
    ax.tick_params(colors="black", labelsize=9)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("black")
    ax.spines["bottom"].set_color("black")
    
    for bar in bars:
        width = bar.get_width()
        ax.text(width + 1.5, bar.get_y() + bar.get_height()/2, f"{width:.1f}%", 
                va="center", ha="left", color="black", fontsize=9)
                
    fig.tight_layout()
    return fig


def plot_confidence_by_algorithm(frame: pd.DataFrame) -> plt.Figure:
    """Plot confidence distributions by sensor / algorithm."""
    fig, ax = plt.subplots(figsize=(7, 5.0), facecolor="white")
    ax.set_facecolor("white")
    
    # Prepare data for boxplot
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
        box = ax.boxplot(data, labels=labels, patch_artist=True, medianprops={"color": "black", "linewidth": 1.5})
        for patch in box["boxes"]:
            patch.set_facecolor(OKABE_ITO_COLORS[2])
            patch.set_edgecolor("black")
            
    ax.set_ylabel("Confidence Score / Value", color="black", fontsize=10)
    ax.set_title("Hotspot Confidence Distribution by Sensor", color="black", fontsize=12, pad=15)
    
    ax.tick_params(colors="black", labelsize=9)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("black")
    ax.spines["bottom"].set_color("black")
    
    fig.tight_layout()
    return fig


def plot_event_concentration(frame: pd.DataFrame) -> plt.Figure:
    """Plot hotspot count by fire event to show spatial concentration."""
    fig, ax = plt.subplots(figsize=(7, 5.0), facecolor="white")
    ax.set_facecolor("white")
    
    # Display top 10 events for readability
    top_events = frame.head(10).copy()
    total_matched = frame["matched_hotspots"].sum()
    
    # Shorten long event names
    labels = []
    for _, row in top_events.iterrows():
        name = str(row["fire_name"])
        if len(name) > 20:
            name = name[:18] + "..."
        labels.append(name)
        
    y_pos = np.arange(len(labels))
    bars = ax.barh(y_pos, top_events["matched_hotspots"], color=OKABE_ITO_COLORS[0], edgecolor="none")
    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels, color="black", fontsize=9)
    ax.invert_yaxis()  # top-down
    ax.set_xlabel("Number of Matched Hotspots", color="black", fontsize=10)
    ax.set_title(f"Concentration of Matches Across Fire Events (Total Matched N={total_matched:,})", color="black", fontsize=12, pad=15)
    
    ax.tick_params(colors="black", labelsize=9)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("black")
    ax.spines["bottom"].set_color("black")
    
    for bar in bars:
        width = bar.get_width()
        ax.text(width + (width * 0.01) + 1, bar.get_y() + bar.get_height()/2, f"{int(width):,}", 
                va="center", ha="left", color="black", fontsize=9)
                
    fig.tight_layout()
    return fig


def plot_pilot_map(hotspots: pd.DataFrame, polygons: List[dict], displayed_n: int) -> plt.Figure:
    """Plot map showing hotspots and fire event boundary polygons."""
    fig, ax = plt.subplots(figsize=(8, 7.0), facecolor="white")
    ax.set_facecolor("white")
    
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
                ax.plot(x, y, color="black", linewidth=1.2, alpha=0.8, zorder=2)
                ax.fill(x, y, color="#999999", alpha=0.15, zorder=1)
                
    # 2. Plot hotspots
    # Filter or sample hotspots
    matched = hotspots[hotspots["match_class"].isin(["bushfire", "prescribed_burn", "other_fire", "spatial_only"])]
    unmatched = hotspots[hotspots["match_class"] == "unmatched"]
    
    # Plot matched
    ax.scatter(matched["longitude"], matched["latitude"], color=OKABE_ITO_COLORS[1], 
               label="Matched Hotspot", s=12, alpha=0.7, zorder=4, marker="o", edgecolors="none")
               
    # Plot unmatched
    ax.scatter(unmatched["longitude"], unmatched["latitude"], color=OKABE_ITO_COLORS[0], 
               label="Unresolved Hotspot", s=8, alpha=0.5, zorder=3, marker="x")
               
    ax.set_xlabel("Longitude (WGS84)", color="black", fontsize=10)
    ax.set_ylabel("Latitude (WGS84)", color="black", fontsize=10)
    ax.set_title(f"Active-Fire Spatial Distribution (Sample Size: {displayed_n:,})", color="black", fontsize=12, pad=15)
    
    ax.legend(facecolor="white", edgecolor="black", labelcolor="black", loc="upper right")
    ax.tick_params(colors="black", labelsize=9)
    ax.grid(True, linestyle="--", alpha=0.3, color="#999999")
    
    fig.tight_layout()
    return fig
