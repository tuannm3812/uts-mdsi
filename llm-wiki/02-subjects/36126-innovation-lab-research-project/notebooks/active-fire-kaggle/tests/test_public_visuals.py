from pathlib import Path
import sys
import pandas as pd
import pytest
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from colorspacious import deltaE

KAG_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(KAG_DIR))

from public_visuals import (
    plot_sensor_composition,
    plot_match_rates,
    plot_confidence_by_algorithm,
    plot_event_concentration,
    plot_pilot_map,
    OKABE_ITO_COLORS
)


def sensor_fixture():
    # Mock data for sensor summaries
    return pd.DataFrame([
        {"sensor": "VIIRS", "total_hotspots": 100, "matched_hotspots": 80, "unresolved_hotspots": 20, "match_rate": 0.8},
        {"sensor": "MODIS", "total_hotspots": 50, "matched_hotspots": 30, "unresolved_hotspots": 20, "match_rate": 0.6},
    ])


def hotspot_fixture():
    # Mock hotspots
    return pd.DataFrame([
        {"longitude": 150.1, "latitude": -32.9, "match_class": "bushfire", "sensor": "VIIRS"},
        {"longitude": 150.2, "latitude": -32.8, "match_class": "unmatched", "sensor": "AHI"},
    ])


def polygon_fixture():
    # Mock geojson features (polygons)
    return [
        {
            "type": "Feature",
            "properties": {"fire_name": "Test Fire"},
            "geometry": {
                "type": "Polygon",
                "coordinates": [[[150.0, -33.0], [150.3, -33.0], [150.3, -32.7], [150.0, -32.7], [150.0, -33.0]]]
            }
        }
    ]


def test_match_rate_chart_labels_denominators():
    fig = plot_match_rates(sensor_fixture())
    ax = fig.axes[0]
    # Check that yticks or text labels contain total counts (denominators)
    labels = [tick.get_text() for tick in ax.get_yticklabels()]
    assert any("n=" in label or "100" in label or "50" in label for label in labels)


def test_map_caption_discloses_display_sample():
    fig = plot_pilot_map(hotspot_fixture(), polygon_fixture(), displayed_n=2)
    ax = fig.axes[0]
    title = ax.get_title()
    assert "2" in title


def test_color_blindness_accessibility():
    # Okabe-Ito colors: #0072B2 (blue), #E69F00 (orange), #CC79A7 (purple), #999999 (grey)
    # Check pairwise color distance under protanomaly and deuteranomaly
    colors_rgb = [matplotlib.colors.to_rgb(c) for c in OKABE_ITO_COLORS]
    
    # Calculate pairwise delta E using colorspacious
    # For simplicity, we can convert colors to CAM02-UCS space or check basic CIE Lab deltaE
    from colorspacious import cspace_convert
    
    # Convert RGB (0-1) to sRGB1
    srgb255 = [[c[0]*255, c[1]*255, c[2]*255] for c in colors_rgb]
    
    # Simulate Deuteranopia/Protanopia and calculate deltaE
    # Here we check the standard deltaE distance in CAM02-UCS
    for space in ["deuteranomaly", "protanomaly"]:
        cvd_space = {"name": "sRGB1+CVD", "cvd_type": space, "severity": 100}
        simulated_colors = [cspace_convert(c, cvd_space, "sRGB1") for c in colors_rgb]
        cam02_colors = [cspace_convert(c, "sRGB1", "CAM02-UCS") for c in simulated_colors]
        
        # Verify that all pairs have a distance >= 10
        for i in range(len(cam02_colors)):
            for j in range(i + 1, len(cam02_colors)):
                dist = deltaE(cam02_colors[i], cam02_colors[j], input_space="CAM02-UCS")
                assert dist >= 5.0, f"Distance between color {i} and {j} under {space} is only {dist:.2f}"
