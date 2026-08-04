import json
import sys
from pathlib import Path
import nbformat as nbf

KAG_DIR = Path(__file__).resolve().parent


def build_notebook(output_path: Path, snapshot_slug: str) -> Path:
    # Read helper script contents
    active_fire_pilot_dir = KAG_DIR.parent / "active-fire-pilot"
    
    # Read match_hotspots.py content
    match_hotspots_code = (active_fire_pilot_dir / "match_hotspots.py").read_text(encoding="utf-8")
    # Remove module docstring
    if match_hotspots_code.startswith('"""'):
        match_hotspots_code = match_hotspots_code[match_hotspots_code.find('"""', 3) + 3:].strip()
        
    # Read public_analysis.py content
    public_analysis_code = (KAG_DIR / "public_analysis.py").read_text(encoding="utf-8")
    
    # Read public_visuals.py content
    public_visuals_code = (KAG_DIR / "public_visuals.py").read_text(encoding="utf-8")
    
    nb = nbf.v4.new_notebook()
    
    cells = []
    
    # Title
    cells.append(nbf.v4.new_markdown_cell(
        "# NSW Active-Fire Reliability Pilot\n\n"
        "> **Important Interpretation Callout:** This notebook performs a spatiotemporal reliability audit "
        "matching satellite hotspot observations (DEA Hotspots) against official post-event fire boundary records "
        "(NPWS Fire History). This is a *calibration and reliability study* of spatial-temporal overlap, "
        "**not a detector-accuracy evaluation**. Unmatched observations are labelled as *unresolved*, "
        "and must not be assumed to be errors or sensor inaccuracies without independent ground truth."
    ))
    
    # Cell 2: Imports and config
    config_code = (
        f'# Execution Configuration\n'
        f'EXECUTION_MODE = "snapshot"  # Options: "snapshot", "live_refresh"\n'
        f'SNAPSHOT_SLUG = "{snapshot_slug}"\n\n'
        f'import json\n'
        f'import hashlib\n'
        f'import os\n'
        f'from pathlib import Path\n'
        f'from datetime import datetime, timedelta, timezone\n'
        f'import math\n'
        f'from typing import Dict, List, Tuple, Optional, Sequence\n'
        f'import pandas as pd\n'
        f'import numpy as np\n'
        f'import matplotlib.pyplot as plt\n'
        f'import matplotlib.colors as mcolors\n'
    )
    cells.append(nbf.v4.new_code_cell(config_code))
    
    # Section 1 Markdown
    cells.append(nbf.v4.new_markdown_cell(
        "## 1. Project overview\n\n"
        "This project evaluates the spatiotemporal reliability of satellite active-fire hotspots in New South Wales (NSW), Australia. "
        "Satellite-derived hotspot products (such as those from MODIS, VIIRS, and AHI) are widely used for real-time fire detection, "
        "but their operational reliability must be calibrated against official historical fire boundaries to understand spatial and "
        "temporal alignment. We focus on a bounded region of NSW during a fortnight of intense fire activity in January 2020."
    ))
    
    # Section 2 Markdown
    cells.append(nbf.v4.new_markdown_cell(
        "## 2. Data and methodology\n\n"
        "We utilize two primary public datasets:\n"
        "1. **DEA Hotspots WFS:** Historical active-fire point observations collected by Geoscience Australia, including attributes like "
        "satellite, sensor, acquisition time, temp_kelvin, power, confidence, and positional accuracy.\n"
        "2. **NPWS Fire History Layer:** Polygon boundaries representing wildfires and prescribed burns managed by the NSW National Parks "
        "and Wildlife Service (NPWS), explicitly licensed under Creative Commons Attribution (CC BY 4.0).\n\n"
        "**Methodology:**\n"
        "- **Exact Matching:** A hotspot point is matched if it falls directly inside a fire boundary polygon, and its observation time "
        "is within the fire's ignition-to-extinguish window (plus a symmetric 1-day temporal grace period).\n"
        "- **Sensor-Buffered Matching:** The match criteria are expanded by buffering the fire polygons using each sensor's documented "
        "positional accuracy (e.g., ±0.375 km for VIIRS, ±1 km for MODIS)."
    ))
    
    # Cell 4: Match hotspots code
    cells.append(nbf.v4.new_code_cell(match_hotspots_code))
    
    # Cell 5: Public analysis code
    cells.append(nbf.v4.new_code_cell(public_analysis_code))
    
    # Cell 6: Public visuals code
    cells.append(nbf.v4.new_code_cell(public_visuals_code))
    
    # Cell 7: Section 3 Results Markdown
    cells.append(nbf.v4.new_markdown_cell(
        "## 3. Results\n\n"
        "We load the datasets from the snapshot package and perform the spatiotemporal matching. We compare the match rates and "
        "unresolved observations between the exact matching baseline and the sensor-buffered matching pipeline."
    ))
    
    main_execution_code = (
        "import re\n\n"
        "def normalize_hotspot(feature: dict) -> dict:\n"
        "    properties = feature.get('properties', {})\n"
        "    coordinates = feature.get('geometry', {}).get('coordinates', [None, None])\n"
        "    return {\n"
        "        'id': properties.get('id'),\n"
        "        'datetime': properties.get('datetime'),\n"
        "        'longitude': properties.get('longitude', coordinates[0]),\n"
        "        'latitude': properties.get('latitude', coordinates[1]),\n"
        "        'sensor': properties.get('sensor'),\n"
        "        'satellite': properties.get('satellite'),\n"
        "        'process_algorithm': properties.get('process_algorithm'),\n"
        "        'confidence': properties.get('confidence'),\n"
        "        'accuracy': properties.get('accuracy'),\n"
        "    }\n\n"
        "def parse_accuracy_km(value) -> float:\n"
        "    if value in (None, ''):\n"
        "        return 0.0\n"
        "    match = re.search(r'([0-9]+(?:\\.[0-9]+)?)', str(value))\n"
        "    return float(match.group(1)) if match else 0.0\n\n"
        "# Helper to map NPWS schema to standard RFS-like fields consumed by matching code\n"
        "def map_npws_to_rfs(feature: dict) -> dict:\n"
        "    props = feature.get('properties', {})\n"
        "    mapped_props = {\n"
        "        'fire_id': props.get('FireNo') or str(props.get('OBJECTID')),\n"
        "        'fire_name': props.get('FireName') or 'Unnamed NPWS Event',\n"
        "        'ignition_date': props.get('StartDate'),\n"
        "        'extinguish_date': props.get('EndDate'),\n"
        "        'fire_type': 'bushfire' if props.get('FireType') == 1 else 'prescribed_burn',\n"
        "        'area_ha': props.get('AreaHa'),\n"
        "        'perim_km': (props.get('PerimeterM') or 0.0) / 1000.0,\n"
        "        'state': 'NSW',\n"
        "        'agency': 'NPWS'\n"
        "    }\n"
        "    return {\n"
        "        'type': feature.get('type'),\n"
        "        'properties': mapped_props,\n"
        "        'geometry': feature.get('geometry')\n"
        "    }\n\n"
        "# Define file paths based on execution mode\n"
        "if EXECUTION_MODE == 'snapshot':\n"
        "    import os\n"
        "    # Check Kaggle input dataset, recursive search, or local fallback\n"
        "    dataset_dir = None\n"
        "    for root, dirs, files in os.walk('/kaggle/input'):\n"
        "        if 'dea_hotspots.geojson' in files:\n"
        "            dataset_dir = Path(root)\n"
        "            print(f\"Found dataset at: {dataset_dir}\")\n"
        "            break\n"
        "    if dataset_dir is None:\n"
        "        for root, dirs, files in os.walk('../input'):\n"
        "            if 'dea_hotspots.geojson' in files:\n"
        "                dataset_dir = Path(root)\n"
        "                print(f\"Found dataset at: {dataset_dir}\")\n"
        "                break\n"
        "    if dataset_dir is None:\n"
        "        dataset_dir = Path('.')\n"
        "        print(f\"Dataset not found in Kaggle inputs. Falling back to local: {dataset_dir}\")\n"
        "    dea_path = dataset_dir / 'dea_hotspots.geojson'\n"
        "    npws_path = dataset_dir / 'npws_fire_history.geojson'\n"
        "else:\n"
        "    # Live refresh (download fresh features)\n"
        "    raise NotImplementedError('Live refresh from ArcGIS/WFS endpoints requires direct network access')\n\n"
        "# Load datasets\n"
        "print('Loading spatial datasets...')\n"
        "with open(dea_path) as f:\n"
        "    dea_data = json.load(f)\n"
        "with open(npws_path) as f:\n"
        "    npws_data = json.load(f)\n\n"
        "# Map and prepare features\n"
        "npws_mapped = [map_npws_to_rfs(f) for f in npws_data['features']]\n"
        "features = prepare_features(npws_mapped)\n"
        "hotspots = [normalize_hotspot(h) for h in dea_data['features']]\n\n"
        "# Perform exact spatiotemporal matching\n"
        "print('Running exact matching...')\n"
        "exact_matches = [classify_hotspot(h, features, grace_days=1, spatial_buffer_km=0.0) for h in hotspots]\n"
        "df_exact = pd.DataFrame(exact_matches)\n\n"
        "# Perform sensor-buffered matching\n"
        "print('Running sensor-buffered matching...')\n"
        "buffered_matches = [classify_hotspot(h, features, grace_days=1, spatial_buffer_km=parse_accuracy_km(h.get('accuracy'))) for h in hotspots]\n"
        "df_buffered = pd.DataFrame(buffered_matches)\n\n"
        "# Compute headline summary metrics\n"
        "headline = headline_summary(df_exact, df_buffered)\n"
        "headline['fire_event_count'] = len(features)\n"
        "print('\\n=== HEADLINE METRICS ===')\n"
        "for k, v in headline.items():\n"
        "    if 'rate' in k:\n"
        "        print(f'{k}: {v * 100.0:.2f}%')\n"
        "    else:\n"
        "        print(f'{k}: {v:,}')\n\n"
        "# Assert snapshot invariants if in snapshot mode\n"
        "expected_invariants = {\n"
        "    'total_hotspots': 19849,\n"
        "    'fire_event_count': 14,\n"
        "    'exact_matches': 15334,\n"
        "    'buffered_matches': 19277,\n"
        "    'buffered_unresolved': 572,\n"
        "}\n"
        "if EXECUTION_MODE == 'snapshot':\n"
        "    assert_snapshot_invariants(headline, expected_invariants)\n"
        "    print('\\n[SUCCESS] Snapshot invariants verified successfully.')\n"
    )
    cells.append(nbf.v4.new_code_cell(main_execution_code))
    
    # Cell 9: Main visualization code
    main_visuals_code = (
        "# 1. Generate and display sensor composition plot\n"
        "fig1 = plot_sensor_composition(pd.DataFrame([\n"
        "    {'sensor': s, 'total_hotspots': count}\n"
        "    for s, count in df_exact.groupby('sensor').size().items()\n"
        "]))\n"
        "plt.show()\n\n"
        "# 2. Generate and display match rates plot\n"
        "df_sensor = sensor_summary(df_buffered)\n"
        "fig2 = plot_match_rates(df_sensor)\n"
        "plt.show()\n\n"
        "# 3. Generate confidence distribution boxplot\n"
        "fig3 = plot_confidence_by_algorithm(df_buffered)\n"
        "plt.show()\n\n"
        "# 4. Generate fire event concentration plot\n"
        "df_concentration = event_concentration(df_buffered)\n"
        "fig4 = plot_event_concentration(df_concentration)\n"
        "plt.show()\n\n"
        "# 5. Generate and display spatial distribution map\n"
        "fig5 = plot_pilot_map(df_buffered, npws_mapped, displayed_n=len(df_buffered))\n"
        "plt.show()\n"
    )
    cells.append(nbf.v4.new_code_cell(main_visuals_code))
    
    # Section 4 Markdown
    cells.append(nbf.v4.new_markdown_cell(
        "## 4. Reliability analysis\n\n"
        "Based on the results, we observe that the exact spatiotemporal match rate of active-fire observations against "
        "the NPWS Fire History is **77.25%** (15,334 of 19,849 hotspots matched). When taking the sensors' spatial positional "
        "accuracy into account via buffering, the match rate increases to **97.12%** (19,277 of 19,849 hotspots matched).\n\n"
        "Crucially, the remaining **2.88%** (572 hotspots) are labeled as **unresolved**. These observations represent "
        "spatiotemporal offsets that could be caused by:\n"
        "1. Positional or temporal drift in the satellite products.\n"
        "2. Off-reserve fire events not captured in the NPWS-specific reserve dataset.\n"
        "3. Small agricultural burns or brief fire events that did not form a mapped boundary.\n\n"
        "This confirms the necessity of using the term *unresolved* rather than assuming they represent errors or omissions, "
        "as they may indicate real fire activity outside of NPWS-managed boundaries."
    ))
    
    # Section 5 Markdown
    cells.append(nbf.v4.new_markdown_cell(
        "## 5. Research implications\n\n"
        "For downstream modeling, this pilot illustrates that spatial and temporal tolerances are critical. "
        "A strict containment check (exact matching) under-reports the alignment of satellite hotspots with actual events. "
        "By buffering the polygons, we align the official data with the sensors' physical limits, resolving the spatiotemporal offsets. "
        "Future research must account for administrative boundaries when analyzing active fires to ensure off-reserve observations "
        "are not mischaracterized as errors."
    ))
    
    # Section 6 Markdown
    cells.append(nbf.v4.new_markdown_cell(
        "## 6. Reproducibility\n\n"
        "To reproduce this analysis, check the local configuration and confirmed data sources:\n\n"
        "### Confirmed Public-Source Attributions:\n"
        "- **DEA Hotspots WFS:** Provided by Geoscience Australia under CC BY 4.0. URL: [DEA Hotspots Service](https://hotspots.dea.ga.gov.au/)\n"
        "- **NPWS Fire History:** Provided by NSW National Parks and Wildlife Service under Creative Commons Attribution. URL: [Data.NSW NPWS Record](https://data.nsw.gov.au/data/dataset/npws-fire-history)\n\n"
        "### Snapshot Provenance Checksums:\n"
        "- `dea_hotspots.geojson` (SHA-256): `e3fef8c1c9b4a81b07482eca2209885dc0b9c5f08fc5c6ddf310ad39313655d3`\n"
        "- `npws_fire_history.geojson` (SHA-256): `990507571b2b028c0d5687a7ba4351adb0b7e60ced1a53eddf9eb30e91f92dd5`"
    ))
    
    # Cell 11: Live refresh code
    live_refresh_code = (
        "# Live Refresh Mode (guarded)\n"
        "if EXECUTION_MODE == 'live_refresh':\n"
        "    # In live refresh mode, we would query the active REST services.\n"
        "    # Since this is a CPU-only private Kaggle runtime with internet disabled by default,\n"
        "    # any live refresh must be triggered in an authorized environment.\n"
        "    print('Initializing live refresh...')\n"
        "    # Rerun code goes here...\n"
    )
    cells.append(nbf.v4.new_code_cell(live_refresh_code))
    
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
    nb.cells = cells
    
    # Save notebook
    with open(output_path, "w", encoding="utf-8") as f:
        nbf.write(nb, f)
        
    return output_path


def main():
    build_notebook(
        KAG_DIR / "2_active_fire_reliability_pilot.ipynb",
        "tuannm3812/nsw-active-fire-pilot-snapshot"
    )
    print("Notebook generated successfully.")


if __name__ == "__main__":
    main()
