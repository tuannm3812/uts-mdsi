import json
from pathlib import Path
import nbformat as nbf

KAG_DIR = Path(__file__).resolve().parent


def build_notebook(output_path: Path, snapshot_slug: str) -> Path:
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
    
    # Environment Check
    cells.append(nbf.v4.new_markdown_cell(
        "### Setup and Environment Check\n\n"
        "We verify standard package versions to ensure reproducible executions."
    ))
    
    config_code = (
        f'# Execution Configuration\n'
        f'EXECUTION_MODE = "snapshot"  # Options: "snapshot", "live_refresh"\n'
        f'SNAPSHOT_SLUG = "{snapshot_slug}"\n\n'
        f'# Spatiotemporal Matching Configurations\n'
        f'TEMPORAL_GRACE_DAYS = 1.0  # Temporal window tolerance in days\n'
        f'DISPLAY_SAMPLE_SIZE = 1000  # Number of hotspots to display on pilot map\n'
        f'RANDOM_SEED = 36126        # Random seed for reproducibility\n\n'
        f'# Standard Library Imports\n'
        f'import json\n'
        f'import hashlib\n'
        f'import os\n'
        f'import sys\n'
        f'from pathlib import Path\n'
        f'from datetime import datetime, timedelta, timezone\n'
        f'import math\n'
        f'from typing import Dict, List, Tuple, Optional, Sequence, Iterable\n\n'
        f'# Third-Party Library Imports\n'
        f'import pandas as pd\n'
        f'import numpy as np\n'
        f'import matplotlib.pyplot as plt\n'
        f'import matplotlib.colors as mcolors\n\n'
        'from importlib.metadata import version\n'
        'print("Runtime Environment:")\n'
        'for pkg in ["pandas", "numpy", "matplotlib", "colorspacious", "nbformat"]:\n'
        '    try:\n'
        '        print(f"- {pkg}: {version(pkg)}")\n'
        '    except Exception:\n'
        '        print(f"- {pkg}: not installed")\n'
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
        "## 2. Methodology & Mathematical Formulation\n\n"
        "To calibrate the spatiotemporal overlap between satellite hotspot observations and historical fire boundaries, we define a formal matching framework. Let a hotspot observation $h$ be represented as:\n"
        "$$h = (\\phi_h, \\lambda_h, t_h, \\text{sensor}(h))$$\n"
        "where $(\\phi_h, \\lambda_h)$ is the geographic position (latitude, longitude), $t_h$ is the acquisition timestamp, and $\\text{sensor}(h)$ designates the observing instrument (e.g., MODIS, VIIRS, AHI).\n\n"
        "A fire event $F_i$ from the historical boundary record is represented as:\n"
        "$$F_i = (P_i, [t_{\\text{ignition}, i}, t_{\\text{extinguish}, i}])$$\n"
        "where $P_i$ is the spatial polygon (or MultiPolygon) boundary, and $[t_{\\text{ignition}, i}, t_{\\text{extinguish}, i}]$ is the active burn interval.\n\n"
        "We evaluate matching under two distinct regimes:\n\n"
        "### A. Exact Spatial Matching (Baseline)\n"
        "A hotspot $h$ is classified as an **exact match** to fire event $F_i$ if it satisfies both spatial containment and temporal window overlap (including a symmetric temporal grace period $\\Delta t$):\n"
        "1. **Spatial Containment:**\n"
        "   $$(\\phi_h, \\lambda_h) \\in P_i$$\n"
        "2. **Temporal Alignment:**\n"
        "   $$t_h \\in [t_{\\text{ignition}, i} - \\Delta t, t_{\\text{extinguish}, i} + \\Delta t]$$\n"
        "We set the temporal grace period to $\\Delta t = 1 \\text{ day}$ to account for reporting latencies and ignition/extinguishment boundary uncertainties.\n\n"
        "### B. Sensor-Buffered Spatial Matching\n"
        "To account for the physical limits and positional accuracy of satellite sensors, we expand the spatial boundary $P_i$ using a sensor-specific buffer $\\epsilon_{s}$. A hotspot $h$ matches $F_i$ under buffered tolerances if:\n"
        "1. **Buffered Spatial Containment:**\n"
        "   $$\\text{dist}((\\phi_h, \\lambda_h), P_i) \\le \\epsilon_{s}$$\n"
        "   where $\\text{dist}$ is the shortest spherical distance from the hotspot coordinates to the boundary of $P_i$:\n"
        "   $$\\text{dist}(h_{\\text{pos}}, P_i) = \\begin{cases} 0 & \\text{if } h_{\\text{pos}} \\in P_i \\\\ \\min_{p \\in \\partial P_i} \\text{dist}_{\\text{great-circle}}(h_{\\text{pos}}, p) & \\text{otherwise} \\end{cases}$$\n"
        "2. **Temporal Alignment:**\n"
        "   $$t_h \\in [t_{\\text{ignition}, i} - \\Delta t, t_{\\text{extinguish}, i} + \\Delta t]$$\n\n"
        "The spatial buffer threshold $\\epsilon_{s}$ is determined by the sensor's native nominal spatial resolution:\n"
        "* **VIIRS:** $\\epsilon_{\\text{VIIRS}} = 0.375\\text{ km}$ (high-resolution channels)\n"
        "* **MODIS:** $\\epsilon_{\\text{MODIS}} = 1.0\\text{ km}$\n"
        "* **AHI:** $\\epsilon_{\\text{AHI}} = 2.0\\text{ km}$"
    ))
    
    # Cell 5: Math & Matching helpers
    cells.append(nbf.v4.new_markdown_cell(
        "### 2.1 Spatiotemporal Containment Core Algorithms\n\n"
        "The core mathematical and containment logic for ray-casting containment checks and segment-distance buffer calculations."
    ))
    cells.append(nbf.v4.new_code_cell(match_hotspots_code))
    
    # Cell 6: Data analysis helpers
    cells.append(nbf.v4.new_markdown_cell(
        "### 2.2 Data Aggregation and Metrics Helpers\n\n"
        "Helper functions to compute statistics, match rates, event concentration distributions, and refresh differences."
    ))
    cells.append(nbf.v4.new_code_cell(public_analysis_code))
    
    # Cell 7: Visuals helpers
    cells.append(nbf.v4.new_markdown_cell(
        "### 2.3 Visualization Helpers\n\n"
        "Functions utilizing the Okabe-Ito colorblind-accessible color palette and Matplotlib version-compatibility checks to render analysis figures."
    ))
    cells.append(nbf.v4.new_code_cell(public_visuals_code))
    
    # Section 3 Markdown
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
        "def parse_accuracy_km(value: Optional[str]) -> float:\n"
        "    if value in (None, ''):\n"
        "        return 0.0\n"
        "    match = re.search(r'([0-9]+(?:\\.[0-9]+)?)', str(value))\n"
        "    return float(match.group(1)) if match else 0.0\n\n"
        "# Helper to map NPWS schema to standard RFS-like fields consumed by matching code\n"
        "def map_npws_to_rfs(feature: dict) -> dict:\n"
        "    props = feature.get('properties', {})\n"
        "    return {\n"
        "        'geometry': feature.get('geometry'),\n"
        "        'properties': {\n"
        "            'fire_id': props.get('FireNo') or str(props.get('OBJECTID')),\n"
        "            'fire_name': props.get('FireName') or 'Unnamed',\n"
        "            'ignition_date': props.get('StartDate'),\n"
        "            'extinguish_date': props.get('EndDate'),\n"
        "            'fire_type': 'bushfire' if props.get('FireType') == 1 else 'prescribed_burn',\n"
        "        }\n"
        "    }\n\n"
        "# 1. Dynamic search of Kaggle/local inputs\n"
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
        "    curr = Path('.').resolve()\n"
        "    for parent in [curr] + list(curr.parents):\n"
        "        candidate = parent / 'output' / 'kaggle' / 'active-fire-pilot'\n"
        "        if (candidate / 'dea_hotspots.geojson').is_file():\n"
        "            dataset_dir = candidate\n"
        "            print(f\"Found local repository dataset at: {dataset_dir}\")\n"
        "            break\n"
        "if dataset_dir is None:\n"
        "    dataset_dir = Path('.')\n"
        "    print(f\"Dataset not found. Falling back to current directory: {dataset_dir}\")\n\n"
        "dea_path = dataset_dir / 'dea_hotspots.geojson'\n"
        "npws_path = dataset_dir / 'npws_fire_history.geojson'\n\n"
        "with open(dea_path) as f:\n"
        "    dea_data = json.load(f)\n"
        "with open(npws_path) as f:\n"
        "    npws_data = json.load(f)\n\n"
        "features = [map_npws_to_rfs(f) for f in npws_data['features']]\n"
        "prepared_features = prepare_features(features)\n\n"
        "normalized_hotspots = [normalize_hotspot(h) for h in dea_data['features']]\n\n"
        "print('Running exact matching...')\n"
        "exact_classified = [classify_hotspot(h, prepared_features, grace_days=TEMPORAL_GRACE_DAYS, spatial_buffer_km=0.0) for h in normalized_hotspots]\n"
        "df_exact = pd.DataFrame(exact_classified)\n\n"
        "print('Running sensor-buffered matching...')\n"
        "buffered_classified = []\n"
        "for h in normalized_hotspots:\n"
        "    accuracy_val = parse_accuracy_km(h.get('accuracy'))\n"
        "    buffered_classified.append(classify_hotspot(h, prepared_features, grace_days=TEMPORAL_GRACE_DAYS, spatial_buffer_km=accuracy_val))\n"
        "df_buffered = pd.DataFrame(buffered_classified)\n\n"
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
    
    # Interpretation of Results
    cells.append(nbf.v4.new_markdown_cell(
        "### Interpretation of Results:\n"
        "- **Exact Matching Baseline:** Containment-only matching yields a 77.25% match rate, leaving 4,515 hotspots unresolved.\n"
        "- **Sensor-Buffered matching:** Expanding containment boundaries by the sensors' spatial resolution tolerances increase the match rate to 97.12%, resolving all but 572 hotspots.\n"
        "- **Context:** While buffering resolves spatial uncertainty at polygon edges, the high baseline match rate (77.25%) is heavily influenced by the spatial-temporal footprints of the fire complexes in this area, which we inspect below."
    ))
    
    # Section 4 Markdown
    cells.append(nbf.v4.new_markdown_cell(
        "## 4. Visual Analysis & Event Concentration\n\n"
        "### The Event Concentration Problem\n"
        "While the headline matching metrics show high overall alignment (77.25% exact, 97.12% buffered), a detailed inspection of the match distribution across individual fire events reveals a severe concentration pattern:\n\n"
        "* **The Dominance of Two Mega-Complexes:** Out of the 14 fire events analyzed in this region, just two events—the **Kerry Ridge** complex (183,647 ha) and the **Gospers Mountain** complex (479,514 ha)—account for **97.97% of all matched hotspots** (with Kerry Ridge alone capturing 85.34% of exact matches and 84.99% of buffered matches).\n"
        "* **Spatial Dominance:** The Gospers Mountain polygon alone covers approximately 4,795 km², representing roughly 21% of the entire 22,500 km² study bounding box.\n"
        "* **The \"Hold-out Event\" Caveat:** Because the statistical sample is almost entirely composed of hotspots from these two massive fire complexes, the reported reliability rates are highly sensitive to their specific characteristics. They **cannot be assumed to generalize** to other regions of New South Wales or to smaller, isolated fire incidents. Any operational performance metrics derived from this pilot are effectively evaluations of these two mega-fires."
    ))
    
    # 4.1 Sensor Composition
    cells.append(nbf.v4.new_markdown_cell(
        "### 4.1 Sensor Composition\n\n"
        "We plot the distribution of raw active-fire hotspots across the different satellite instruments in our snapshot."
    ))
    cells.append(nbf.v4.new_code_cell(
        "fig1 = plot_sensor_composition(pd.DataFrame([\n"
        "    {'sensor': s, 'total_hotspots': count}\n"
        "    for s, count in df_exact.groupby('sensor').size().items()\n"
        "]))\n"
        "plt.show()"
    ))
    sensor_composition_takeaway_code = (
        "sensor_counts = df_exact['sensor'].value_counts()\n"
        "total = len(df_exact)\n"
        "pcts = (sensor_counts / total * 100).to_dict()\n"
        "dominant_sensor = sensor_counts.index[0]\n"
        "dominant_pct = pcts[dominant_sensor]\n\n"
        "takeaway = f\"\"\"**Sensor Composition Takeaway:**\n"
        "Geostationary {dominant_sensor} dominates the hotspot observation count (representing {dominant_pct:.1f}% of all detections) due to its high temporal update frequency (every 10 minutes). \"\"\"\n"
        "parts = []\n"
        "for sensor, pct in sorted(pcts.items(), key=lambda x: x[1], reverse=True)[1:]:\n"
        "    parts.append(f\"{sensor} accounts for {pct:.1f}%\")\n"
        "takeaway += \", \".join(parts) + \" of the total dataset.\"\n"
        "from IPython.display import display, Markdown\n"
        "display(Markdown(takeaway))"
    )
    cells.append(nbf.v4.new_code_cell(sensor_composition_takeaway_code))
    
    # 4.2 Match Rates
    cells.append(nbf.v4.new_markdown_cell(
        "### 4.2 Match Rates by Sensor\n\n"
        "We plot the match rate of each sensor type to evaluate spatiotemporal reliability."
    ))
    cells.append(nbf.v4.new_code_cell(
        "df_sensor = sensor_summary(df_buffered)\n"
        "fig2 = plot_match_rates(df_sensor)\n"
        "plt.show()"
    ))
    match_rates_takeaway_code = (
        "df_sensor_stats = sensor_summary(df_buffered)\n"
        "sensor_rates = {row['sensor']: row['match_rate'] * 100 for _, row in df_sensor_stats.iterrows()}\n"
        "sorted_rates = sorted(sensor_rates.items(), key=lambda x: x[1], reverse=True)\n"
        "rates_str = \", \".join([f\"{sensor} at {rate:.2f}%\" for sensor, rate in sorted_rates])\n\n"
        "takeaway = f\"\"\"**Match Rates Takeaway:**\n"
        "Under sensor-buffered matching thresholds, {rates_str}. The higher match rates reflect how spatial buffers compensate for nominal grid-cell sizes, especially for high-resolution polar-orbiting sensors.\"\"\"\n"
        "from IPython.display import display, Markdown\n"
        "display(Markdown(takeaway))"
    )
    cells.append(nbf.v4.new_code_cell(match_rates_takeaway_code))
    
    # 4.3 Confidence Distributions
    cells.append(nbf.v4.new_markdown_cell(
        "### 4.3 Confidence Distribution\n\n"
        "We evaluate the distribution of confidence values across sensors."
    ))
    cells.append(nbf.v4.new_code_cell(
        "fig3 = plot_confidence_by_algorithm(df_buffered)\n"
        "plt.show()"
    ))
    confidence_takeaway_code = (
        "modis_conf = df_buffered[df_buffered['sensor'] == 'MODIS']['confidence'].dropna()\n"
        "modis_median = modis_conf.median() if not modis_conf.empty else 0.0\n"
        "modis_fixed_50 = (modis_conf == 50).mean() * 100 if not modis_conf.empty else 0.0\n\n"
        "viirs_conf = df_buffered[df_buffered['sensor'] == 'VIIRS']['confidence'].dropna()\n"
        "viirs_median = viirs_conf.median() if not viirs_conf.empty else 0.0\n"
        "viirs_discrete_pct = viirs_conf.isin([7, 8, 9, 'low', 'nominal', 'high']).mean() * 100 if not viirs_conf.empty else 0.0\n\n"
        "takeaway = f\"\"\"**Confidence Distributions Takeaway:**\n"
        "The confidence distributions reveal a mixed algorithmic scaling model across sensors rather than a clean split:\n"
        "- **MODIS:** Median confidence is {modis_median:.1f}%. Approximately {modis_fixed_50:.1f}% of the records are fixed at exactly 50 due to SRSS algorithm defaults, while the remaining subset uses a continuous scale.\n"
        "- **VIIRS:** Uses a hybrid scheme. Approximately {viirs_discrete_pct:.1f}% of the records utilize discrete values (such as 7, 8, 9 for the AFIMG algorithm), while a continuous scale is used for other algorithm variants (with an overall median confidence value of {viirs_median:.1f}).\"\"\"\n"
        "from IPython.display import display, Markdown\n"
        "display(Markdown(takeaway))"
    )
    cells.append(nbf.v4.new_code_cell(confidence_takeaway_code))
    
    # 4.4 Fire Event Concentration
    cells.append(nbf.v4.new_markdown_cell(
        "### 4.4 Match Concentration Across Fire Events\n\n"
        "We evaluate the concentration of hotspot matches across the 14 fire events."
    ))
    cells.append(nbf.v4.new_code_cell(
        "df_concentration = event_concentration(df_buffered)\n"
        "fig4 = plot_event_concentration(df_concentration)\n"
        "plt.show()"
    ))
    cells.append(nbf.v4.new_markdown_cell(
        "**Event Concentration Takeaway:**\n"
        "The bar chart confirms the severe concentration of matched hotspots: **Kerry Ridge** accounts for over 16,000 matches, and **Gospers Mountain** accounts for over 2,400 matches. Together they account for 97.97% of matches, highlighting the spatial-temporal scale skew."
    ))
    
    # 4.5 Spatial Distribution Map
    cells.append(nbf.v4.new_markdown_cell(
        "### 4.5 Spatial Distribution Map\n\n"
        "We plot the map showing matched and unresolved hotspots overlaid on fire boundaries."
    ))
    cells.append(nbf.v4.new_code_cell(
        "fig5 = plot_pilot_map(df_buffered, features, displayed_n=DISPLAY_SAMPLE_SIZE)\n"
        "plt.show()"
    ))
    cells.append(nbf.v4.new_markdown_cell(
        "**Spatial Map Takeaway:**\n"
        "Unresolved hotspots (marked by 'x') are mostly located outside the boundary of the reserves or on the outer edges of Gospers Mountain and Kerry Ridge. This confirms that spatial buffer thresholds resolve border matches, but active fires outside reserve boundaries remain unmatched (unresolved)."
    ))
    
    # Section 5 Markdown
    cells.append(nbf.v4.new_markdown_cell(
        "## 5. Research Implications\n\n"
        "### Incident-Level vs. Complex-Level Confound\n"
        "The transition to the NPWS Fire History layer (implemented to comply with CC BY 4.0 licensing) introduced a major methodological change:\n"
        "* **NSW RFS Feature Service:** Logs granular, localized, short-duration *incident-level* records.\n"
        "* **NPWS Fire History:** Represents consolidated, whole-of-season *fire-complex* boundaries (e.g., the Gospers Mountain record spans 107 active days from 25 Oct 2019 to 9 Feb 2020).\n\n"
        "This change in source shifted the scientific unit of analysis from a localized fire front to a massive, long-lived mega-complex. Because a hotspot is statistically much more likely to intersect a 4,795 km² polygon that remains open for over three months, the observed match-rate jump (from 14.5% to 77.25% exact) is driven by this **complex-level spatial-temporal scale confound**, rather than an intrinsic improvement in the operational sensor performance or label reliability.\n\n"
        "### Modeling Recommendations\n"
        "For downstream machine learning and active-fire modeling:\n"
        "1. **Validation Design:** Models evaluated on datasets dominated by mega-complexes will overfit to their specific temporal and spatial footprints. Validation frameworks must implement **split-complex cross-validation**, where entire large complexes (like Gospers Mountain) are held out during training to test generalization on smaller, independent fires.\n"
        "2. **Buffer Attribution:** While spatial buffering increases the match rate to 97.12%, its role must not be overstated. Exact matching is already 77.25% because of the immense size of the target polygons; buffering only resolves minor edge-drift (accounting for a ~20% marginal increase).\n\n"
        "### Project Context and Roadmap\n"
        "This notebook is the data-quality foundation stage of a larger applied research project, not a standalone endpoint. The reliability findings above — particularly the event-concentration and reference-granularity confounds — directly inform the next stage: building a confidence-filtered, multi-decade active-fire hotspot dataset fused with auxiliary weather and vegetation/land-cover covariates, for short-horizon (1–7 day) hotspot forecasting using a multimodal spatiotemporal transformer with cross-modal attention fusion. This pilot is not a fire-prediction system; it establishes the reference-data reliability constraints that any downstream predictive model built on this data must account for."
    ))
    
    # Section 6 Markdown
    cells.append(nbf.v4.new_markdown_cell(
        "## 6. Reproducibility\n\n"
        "To reproduce this analysis, check the local configuration and confirmed data sources:\n\n"
        "### Confirmed Public-Source Attributions:\n"
        "- **DEA Hotspots WFS:** Provided by Geoscience Australia under CC BY 4.0. URL: [DEA Hotspots Service](https://hotspots.dea.ga.gov.au/)\n"
        "- **NPWS Fire History:** Provided by NSW National Parks and Wildlife Service under Creative Commons Attribution. URL: [Data.NSW NPWS Record](https://data.nsw.gov.au/data/dataset/fire-history-wildfires-and-prescribed-burns-1e8b6)\n\n"
        "### Snapshot Provenance Checksums:\n"
        "- `dea_hotspots.geojson` (SHA-256): `e3fef8c1c9b4a81b07482eca2209885dc0b9c5f08fc5c6ddf310ad39313655d3`\n"
        "- `npws_fire_history.geojson` (SHA-256): `990507571b2b028c0d5687a7ba4351adb0b7e60ced1a53eddf9eb30e91f92dd5`"
    ))
    
    # JSON Snapshot Cell
    snapshot_code = (
        "import json\n"
        "snapshot = {\n"
        "    \"total_hotspots\": int(headline[\"total_hotspots\"]),\n"
        "    \"exact_matches\": int(headline[\"exact_matches\"]),\n"
        "    \"exact_match_rate\": round(headline[\"exact_match_rate\"], 4),\n"
        "    \"buffered_matches\": int(headline[\"buffered_matches\"]),\n"
        "    \"buffered_match_rate\": round(headline[\"buffered_match_rate\"], 4),\n"
        "    \"buffered_unresolved\": int(headline[\"buffered_unresolved\"]),\n"
        "}\n"
        "print(\"=== REPRODUCIBILITY SNAPSHOT ===\")\n"
        "print(json.dumps(snapshot, indent=2))"
    )
    cells.append(nbf.v4.new_code_cell(snapshot_code))
    
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


def main() -> None:
    build_notebook(
        KAG_DIR / "2_active_fire_reliability_pilot.ipynb",
        "tuannm3812/nsw-active-fire-pilot-snapshot"
    )
    print("Notebook generated successfully.")


if __name__ == "__main__":
    main()
