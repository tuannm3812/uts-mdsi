import json
from pathlib import Path
import nbformat as nbf

KAG_DIR = Path(__file__).resolve().parent


def build_eda_notebook(output_path: Path, snapshot_slug: str) -> Path:
    nb = nbf.v4.new_notebook()
    cells = []
    
    # Title
    cells.append(nbf.v4.new_markdown_cell(
        "# NSW Active-Fire Reliability Pilot - Exploratory Data Analysis (EDA)\n\n"
        "This notebook performs exploratory data analysis on the active-fire hotspots dataset "
        "and NPWS fire history boundaries to understand spatial distributions, temporal offsets, "
        "and sensor-specific characteristics."
    ))
    
    # Imports and Config
    config_code = (
        f'# Execution Configuration\n'
        f'EXECUTION_MODE = "snapshot"  # Options: "snapshot"\n'
        f'SNAPSHOT_SLUG = "{snapshot_slug}"\n\n'
        f'import json\n'
        f'import os\n'
        f'from pathlib import Path\n'
        f'from datetime import datetime, timezone\n'
        f'import pandas as pd\n'
        f'import numpy as np\n'
        f'import matplotlib.pyplot as plt\n'
        f'import matplotlib.colors as mcolors\n'
    )
    cells.append(nbf.v4.new_code_cell(config_code))
    
    # Path Resolution and Loading
    load_code = (
        "# Locate and load the snapshot dataset\n"
        "dataset_dir = None\n"
        "for root, dirs, files in os.walk('/kaggle/input'):\n"
        "    if 'dea_hotspots.geojson' in files:\n"
        "        dataset_dir = Path(root)\n"
        "        print(f\"Found dataset at: {dataset_dir}\")\n"
        "        break\n"
        "if dataset_dir is None:\n"
        "    for root, dirs, files in os.walk('../input'):\n"
        "        if 'dea_hotspots.geojson' in files:\n"
        "            dataset_dir = Path(root)\n"
        "            print(f\"Found dataset at: {dataset_dir}\")\n"
        "            break\n"
        "if dataset_dir is None:\n"
        "    dataset_dir = Path('.')\n"
        "    print(f\"Dataset not found in Kaggle inputs. Falling back to local: {dataset_dir}\")\n\n"
        "dea_path = dataset_dir / 'dea_hotspots.geojson'\n"
        "npws_path = dataset_dir / 'npws_fire_history.geojson'\n\n"
        "print('Loading spatial datasets...')\n"
        "with open(dea_path) as f:\n"
        "    dea_data = json.load(f)\n"
        "with open(npws_path) as f:\n"
        "    npws_data = json.load(f)\n\n"
        "print(f\"Loaded {len(dea_data['features']):,} hotspots and {len(npws_data['features']):,} fire polygons.\")"
    )
    cells.append(nbf.v4.new_code_cell(load_code))
    
    # Data Normalization
    normalization_code = (
        "# Normalize datasets into pandas DataFrames\n"
        "hotspots_list = []\n"
        "for feature in dea_data['features']:\n"
        "    props = feature.get('properties', {})\n"
        "    geom = feature.get('geometry', {})\n"
        "    coords = geom.get('coordinates', [np.nan, np.nan])\n"
        "    hotspots_list.append({\n"
        "        'id': props.get('id'),\n"
        "        'datetime': pd.to_datetime(props.get('datetime')),\n"
        "        'longitude': props.get('longitude', coords[0]),\n"
        "        'latitude': props.get('latitude', coords[1]),\n"
        "        'sensor': props.get('sensor'),\n"
        "        'satellite': props.get('satellite'),\n"
        "        'temp_kelvin': props.get('temp_kelvin'),\n"
        "        'power': props.get('power'),\n"
        "        'confidence': props.get('confidence'),\n"
        "        'accuracy': props.get('accuracy'),\n"
        "    })\n"
        "df_hotspots = pd.DataFrame(hotspots_list)\n\n"
        "fires_list = []\n"
        "for feature in npws_data['features']:\n"
        "    props = feature.get('properties', {})\n"
        "    fires_list.append({\n"
        "        'fire_id': props.get('FireNo') or str(props.get('OBJECTID')),\n"
        "        'fire_name': props.get('FireName') or 'Unnamed',\n"
        "        'ignition_date': pd.to_datetime(props.get('StartDate')),\n"
        "        'extinguish_date': pd.to_datetime(props.get('EndDate')),\n"
        "        'area_ha': props.get('AreaHa'),\n"
        "        'perimeter_m': props.get('PerimeterM')\n"
        "    })\n"
        "df_fires = pd.DataFrame(fires_list)\n\n"
        "print('Hotspots head:')\n"
        "display(df_hotspots.head())\n"
        "print('\\nFires head:')\n"
        "display(df_fires.head())"
    )
    cells.append(nbf.v4.new_code_cell(normalization_code))
    
    # Spatial EDA Section
    cells.append(nbf.v4.new_markdown_cell(
        "## 1. Spatial Distribution Analysis\n\n"
        "Let us visualize the spatial distribution of hotspots colored by sensor, overlaying the fire boundary polygons."
    ))
    
    spatial_plot_code = (
        "fig, ax = plt.subplots(figsize=(10, 8), facecolor='white')\n"
        "ax.set_facecolor('white')\n\n"
        "OKABE_ITO_COLORS = ['#0072B2', '#E69F00', '#CC79A7', '#999999']\n"
        "sensors = df_hotspots['sensor'].unique()\n\n"
        "# 1. Plot boundary outlines\n"
        "for feature in npws_data['features']:\n"
        "    geom = feature.get('geometry', {})\n"
        "    coords = geom.get('coordinates', [])\n"
        "    poly_list = [coords] if geom.get('type') == 'Polygon' else coords\n"
        "    for poly in poly_list:\n"
        "        for ring in poly:\n"
        "            x = [pt[0] for pt in ring]\n"
        "            y = [pt[1] for pt in ring]\n"
        "            ax.plot(x, y, color='black', linewidth=1.0, alpha=0.7, zorder=2)\n"
        "            ax.fill(x, y, color='#999999', alpha=0.1, zorder=1)\n\n"
        "# 2. Scatter plot hotspots per sensor\n"
        "for idx, sensor in enumerate(sensors):\n"
        "    subset = df_hotspots[df_hotspots['sensor'] == sensor]\n"
        "    ax.scatter(subset['longitude'], subset['latitude'], \n"
        "               color=OKABE_ITO_COLORS[idx % len(OKABE_ITO_COLORS)], \n"
        "               label=f\"{sensor} (n={len(subset):,})\", s=10, alpha=0.6, zorder=3)\n\n"
        "ax.set_xlabel('Longitude')\n"
        "ax.set_ylabel('Latitude')\n"
        "ax.set_title(f\"Active-Fire Spatial Distribution Overlay (Total Hotspots N={len(df_hotspots):,})\", fontsize=12, pad=15)\n"
        "ax.legend(facecolor='white', edgecolor='black')\n"
        "ax.grid(True, linestyle='--', alpha=0.3, color='#999999')\n"
        "plt.tight_layout()\n"
        "plt.show()"
    )
    cells.append(nbf.v4.new_code_cell(spatial_plot_code))
    
    # Temporal EDA Section
    cells.append(nbf.v4.new_markdown_cell(
        "## 2. Sensor Attribute Relationships\n\n"
        "Let us explore the relationship between fire radiative power (FRP / power), temperature (Kelvin), "
        "and confidence scores across different sensors."
    ))
    
    attr_plot_code = (
        "fig, axes = plt.subplots(1, 2, figsize=(14, 5), facecolor='white')\n"
        "for ax in axes:\n"
        "    ax.set_facecolor('white')\n\n"
        "# Left: Scatter plot power vs temperature\n"
        "for idx, sensor in enumerate(sensors):\n"
        "    subset = df_hotspots[df_hotspots['sensor'] == sensor]\n"
        "    axes[0].scatter(subset['temp_kelvin'], subset['power'], \n"
        "                    color=OKABE_ITO_COLORS[idx % len(OKABE_ITO_COLORS)], \n"
        "                    label=sensor, s=12, alpha=0.5)\n"
        "axes[0].set_xlabel('Temperature (Kelvin)')\n"
        "axes[0].set_ylabel('Fire Radiative Power (MW)')\n"
        "axes[0].set_title('Power vs Temperature by Sensor')\n"
        "axes[0].legend(facecolor='white', edgecolor='black')\n"
        "axes[0].grid(True, linestyle='--', alpha=0.3, color='#999999')\n\n"
        "# Right: Boxplot of confidence values per sensor\n"
        "box_data = []\n"
        "box_labels = []\n"
        "for sensor in sorted(sensors):\n"
        "    subset = df_hotspots[df_hotspots['sensor'] == sensor]['confidence'].dropna()\n"
        "    if not subset.empty:\n"
        "        box_data.append(subset.values)\n"
        "        box_labels.append(f\"{sensor}\\n(n={len(subset):,})\")\n\n"
        "# Check Matplotlib version for boxplot argument compatibility\n"
        "import re\n"
        "import matplotlib\n"
        "try:\n"
        "    v_parts = [int(x) for x in re.findall(r'\\d+', matplotlib.__version__)]\n"
        "except Exception:\n"
        "    v_parts = [3, 0]\n"
        "use_tick_labels = len(v_parts) >= 2 and (v_parts[0] > 3 or (v_parts[0] == 3 and v_parts[1] >= 9))\n\n"
        "if use_tick_labels:\n"
        "    box = axes[1].boxplot(box_data, tick_labels=box_labels, patch_artist=True)\n"
        "else:\n"
        "    box = axes[1].boxplot(box_data, labels=box_labels, patch_artist=True)\n\n"
        "for patch in box['boxes']:\n"
        "    patch.set_facecolor('#CC79A7')\n"
        "    patch.set_edgecolor('black')\n\n"
        "axes[1].set_ylabel('Confidence Value')\n"
        "axes[1].set_title('Confidence Value Distribution by Sensor')\n"
        "plt.tight_layout()\n"
        "plt.show()"
    )
    cells.append(nbf.v4.new_code_cell(attr_plot_code))
    
    # Summary Invariants validation cell
    invariants_code = (
        "# Verify basic dataset invariants match expected snapshot sizes\n"
        "assert len(df_hotspots) == 19849, f\"Expected 19,849 hotspots, got {len(df_hotspots):,}\"\n"
        "assert len(df_fires) == 14, f\"Expected 14 fire boundary features, got {len(df_fires):,}\"\n"
        "print('[PASS] Basic EDA invariants verified successfully.')"
    )
    cells.append(nbf.v4.new_code_cell(invariants_code))
    
    nb.cells = cells
    
    nb.metadata = {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "name": "python"
        }
    }
    
    with open(output_path, "w", encoding="utf-8") as f:
        nbf.write(nb, f)
        
    return output_path


def main():
    build_eda_notebook(
        KAG_DIR / "1_active_fire_eda.ipynb",
        "tuannm3812/nsw-active-fire-pilot-snapshot"
    )
    print("EDA Notebook generated successfully.")


if __name__ == "__main__":
    main()
