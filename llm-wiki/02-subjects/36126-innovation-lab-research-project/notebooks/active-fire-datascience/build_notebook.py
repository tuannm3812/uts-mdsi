"""Build the exploratory EDA + feature-engineering notebook.

Kaggle kernels only receive the notebook file itself -- no sibling .py files,
no arbitrary local paths. The first version of this generator imported from
analysis.py directly and assumed 'data/' was the working directory; both
worked locally (nbconvert runs with this folder as cwd) and both failed on
Kaggle (ModuleNotFoundError, then the same problem would have hit the data
paths) -- see T-042. Fixed by embedding analysis.py's source as a literal
code cell (same pattern notebooks/active-fire-kaggle/build_notebook.py uses,
now understood firsthand rather than just copied) and by walking
/kaggle/input to find the mounted dataset directory at runtime.
"""

import json
from pathlib import Path
import nbformat as nbf

HERE = Path(__file__).resolve().parent


def build_notebook(output_path: Path) -> Path:
    nb = nbf.v4.new_notebook()
    cells = []

    cells.append(nbf.v4.new_markdown_cell(
        "# NSW Active-Fire Data Science Exploration\n\n"
        "**Private, exploratory notebook** -- not the public reproducibility artifact "
        "(`notebooks/active-fire-kaggle/`). This widens the case-study window beyond the "
        "original 14-day reliability pilot to look at real hotspot, weather, and land-cover "
        "data together, and prototype the auxiliary-data features the eventual multimodal "
        "forecasting model (D-011/D-012, Option B) will need.\n\n"
        "**Region:** Greater Blue Mountains bbox (same as the reliability pilot). "
        "**Window:** 15 Dec 2019 -- 15 Jan 2020, chosen after checking live record counts across "
        "several candidate windows -- this one spans the Black Summer activity surge in December "
        "into the original pilot's quieter January window (133,286 DEA hotspot records vs. the "
        "pilot's 19,849 for 14 days), giving real temporal variation to explore rather than a flat "
        "peak. **Not yet the confirmed case-study region/horizon** -- those are still open questions "
        "for Friday's meeting (see `assignments/week-02-mentor-meeting-prep-2026-08-07.md`); this is "
        "prototyping the *process*, reusable once the real scope is frozen."
    ))

    # --- Section 1: Setup ---
    cells.append(nbf.v4.new_markdown_cell("## 1. Setup"))
    cells.append(nbf.v4.new_code_cell(
        "import json\n"
        "import os\n"
        "from pathlib import Path\n"
        "import matplotlib.pyplot as plt\n"
        "import pandas as pd"
    ))

    analysis_source = (HERE / "analysis.py").read_text()
    # Kaggle kernels don't receive sibling .py files -- embed analysis.py's
    # source directly, same reason notebooks/active-fire-kaggle/ does this.
    cells.append(nbf.v4.new_markdown_cell(
        "### Analysis functions\n\nEmbedded from `analysis.py` (Kaggle kernels don't receive sibling files)."
    ))
    cells.append(nbf.v4.new_code_cell(analysis_source))

    config = json.loads((HERE / "config.json").read_text())
    cells.append(nbf.v4.new_code_cell(
        "# Same config.json used to fetch this data locally, inlined for the same reason as above.\n"
        f"config = {json.dumps(config, indent=4)}\n\n"
        "# Find the mounted dataset directory on Kaggle, falling back to the local\n"
        "# dev-time 'data/' folder when run outside Kaggle.\n"
        "DATA_DIR = None\n"
        "for root, dirs, files in os.walk('/kaggle/input'):\n"
        "    if 'dea_hotspots_wide.geojson' in files:\n"
        "        DATA_DIR = Path(root)\n"
        "        break\n"
        "if DATA_DIR is None:\n"
        "    DATA_DIR = Path('data')\n"
        "print(f'Using data directory: {DATA_DIR}')\n"
        "config"
    ))

    # --- Section 2: Hotspot EDA ---
    cells.append(nbf.v4.new_markdown_cell(
        "## 2. Hotspot EDA (MODIS/VIIRS/AHI, DEA Hotspots WFS)\n\n"
        "Widened window vs. the original reliability pilot's 14-day snapshot -- enough range to "
        "look at day-to-day variation, not just a single-event footprint."
    ))
    cells.append(nbf.v4.new_code_cell(
        "hotspots = load_hotspots(DATA_DIR / 'dea_hotspots_wide.geojson')\n"
        "print(f'{len(hotspots):,} hotspot records, {hotspots[\"date\"].nunique()} distinct days')\n"
        "hotspots.head()"
    ))
    cells.append(nbf.v4.new_code_cell(
        "daily_counts = daily_hotspot_counts(hotspots)\n"
        "fig, ax = plt.subplots(figsize=(11, 4))\n"
        "ax.bar(daily_counts['date'].astype(str), daily_counts['hotspot_count'], color='#c0392b')\n"
        "ax.set_title('Daily hotspot count, 15 Dec 2019 - 15 Jan 2020 (Greater Blue Mountains bbox)')\n"
        "ax.set_ylabel('Hotspot count')\n"
        "ax.tick_params(axis='x', rotation=90, labelsize=7)\n"
        "fig.tight_layout()\n"
        "plt.show()"
    ))
    cells.append(nbf.v4.new_markdown_cell(
        "### Sensor composition and per-sensor confidence\n\n"
        "Confidence is reported on different scales per sensor (numeric for some, coarse "
        "nominal/high for others -- this project found that the hard way before, see T-025). "
        "Reporting per-sensor stats rather than one pooled number."
    ))
    cells.append(nbf.v4.new_code_cell(
        "composition = sensor_composition(hotspots)\n"
        "print('Sensor composition:', composition)\n"
        "confidence_summary(hotspots)"
    ))

    # --- Section 3: Weather EDA ---
    cells.append(nbf.v4.new_markdown_cell(
        "## 3. Weather EDA (SILO, gridded daily climate)\n\n"
        "Three points spanning the bbox (north/centroid/south) -- checking whether weather is "
        "roughly uniform across the region or varies enough to matter for a spatial model. "
        "**SILO does not provide wind speed/direction** (checked against SILO's own variable list) "
        "-- flagged rather than silently omitted; wind will need BOM station data or ERA5 later."
    ))
    cells.append(nbf.v4.new_code_cell(
        "weather = load_weather(DATA_DIR, [p['name'] for p in config['silo_grid_points']])\n"
        "weather['centroid'][['date', 'daily_rain', 'max_temp', 'min_temp', 'vp_deficit', 'rh_tmax']].head()"
    ))
    cells.append(nbf.v4.new_code_cell(
        "fig, axes = plt.subplots(2, 1, figsize=(11, 7), sharex=True)\n"
        "for name, df in weather.items():\n"
        "    axes[0].plot(df['date'], df['max_temp'], label=f'{name} max temp')\n"
        "    axes[1].bar(df['date'], df['daily_rain'], alpha=0.5, label=f'{name} rainfall')\n"
        "axes[0].set_title('Max temperature across the 3 grid points')\n"
        "axes[0].legend(fontsize=8)\n"
        "axes[1].set_title('Daily rainfall across the 3 grid points')\n"
        "axes[1].legend(fontsize=8)\n"
        "plt.xticks(rotation=90, fontsize=7)\n"
        "fig.tight_layout()\n"
        "plt.show()"
    ))

    # --- Section 4: Hotspot-weather correlation ---
    cells.append(nbf.v4.new_markdown_cell(
        "## 4. Does dryness track hotspot activity?\n\n"
        "Rough sanity check, not a rigorous causal claim -- rolling rainfall/temperature "
        "features (candidates for the forecasting model) against the daily hotspot count."
    ))
    cells.append(nbf.v4.new_code_cell(
        "weather_features = rolling_dryness_features(weather['centroid'])\n"
        "merged = merge_hotspots_weather(daily_counts, weather_features)\n"
        "merged[['date', 'hotspot_count', 'rain_7d_sum', 'consecutive_dry_days', 'max_temp_7d_mean', 'vpd_7d_mean']]"
    ))
    cells.append(nbf.v4.new_code_cell(
        "fig, ax1 = plt.subplots(figsize=(11, 4))\n"
        "ax1.bar(merged['date'].astype(str), merged['hotspot_count'], color='#c0392b', alpha=0.6, label='Hotspot count')\n"
        "ax1.set_ylabel('Hotspot count', color='#c0392b')\n"
        "ax2 = ax1.twinx()\n"
        "ax2.plot(merged['date'].astype(str), merged['consecutive_dry_days'], color='#2980b9', label='Consecutive dry days')\n"
        "ax2.set_ylabel('Consecutive dry days', color='#2980b9')\n"
        "plt.title('Hotspot count vs. consecutive dry days (centroid point)')\n"
        "ax1.tick_params(axis='x', rotation=90, labelsize=7)\n"
        "fig.tight_layout()\n"
        "plt.show()\n\n"
        "correlation = merged[['hotspot_count', 'rain_7d_sum', 'consecutive_dry_days', 'max_temp_7d_mean', 'vpd_7d_mean']].corr()['hotspot_count']\n"
        "print('Correlation with daily hotspot count:')\n"
        "print(correlation)"
    ))

    # --- Section 5: Land cover ---
    cells.append(nbf.v4.new_markdown_cell(
        "## 5. Land cover at hotspot locations (DEA Land Cover, Landsat)\n\n"
        "Sampled a subset of unique hotspot locations (not all ~130k -- see `fetch_landcover.py` "
        "for why: one WMS call per unique location, and hotspots cluster heavily in space, so a "
        "few hundred samples already covers most of the distinct land-cover classes present)."
    ))
    cells.append(nbf.v4.new_code_cell(
        "landcover = load_landcover(DATA_DIR / 'landcover_sample.json')\n"
        "print(f'{len(landcover)} locations resolved')\n"
        "distribution = landcover_class_distribution(landcover)\n"
        "distribution"
    ))
    cells.append(nbf.v4.new_code_cell(
        "fig, ax = plt.subplots(figsize=(9, 4))\n"
        "distribution.plot(kind='barh', ax=ax, color='#27ae60')\n"
        "ax.set_title('Land-cover class at sampled hotspot locations')\n"
        "ax.set_xlabel('Count')\n"
        "fig.tight_layout()\n"
        "plt.show()"
    ))

    # --- Section 6: Candidate features ---
    cells.append(nbf.v4.new_markdown_cell(
        "## 6. Candidate features for the forecasting model\n\n"
        "Not a final feature set -- a working list from this exploration, to refine once the "
        "case-study region/horizon are frozen (Friday's meeting).\n\n"
        "**Hotspot-history branch:**\n"
        "- Rolling hotspot density (count in past N days, within a spatial radius)\n"
        "- Per-sensor confidence, kept separate rather than pooled (per-sensor scales differ)\n"
        "- Fire radiative power (`power`) and brightness temperature (`temp_kelvin`) -- present in "
        "the raw DEA Hotspots data, not used in the original reliability pilot, worth testing as "
        "intensity signals\n"
        "- Day-of-year / seasonality\n\n"
        "**Weather branch (SILO):**\n"
        "- Rolling cumulative rainfall (7/14-day) and consecutive dry-day count -- both show up "
        "in the correlation check above\n"
        "- Vapour pressure deficit (rolling mean) -- a standard fire-danger driver\n"
        "- Max-temperature rolling mean\n"
        "- **Gap:** no wind from SILO -- needs BOM or ERA5 before this branch is complete, since "
        "wind is one of the four variables Arnick explicitly named\n\n"
        "**Land-cover branch (DEA Land Cover):**\n"
        "- Categorical land-cover class (`level3`/`level4`) at each hotspot location\n"
        "- Annual product only (not sub-annual vegetation *condition* -- e.g. dryness/greenness "
        "indices like NDVI would need a separate source, e.g. Sentinel-2, already in the literature "
        "scan's evidence table)\n\n"
        "**Label-confidence branch (this project's own Phase 1 work):**\n"
        "- Reuse the confirmed/unresolved/confirmed-non-fire classification from the reliability "
        "audit (T-009) as a training-time confidence weight, not just a filter -- the literature "
        "scan's innovation angle #1"
    ))

    cells.append(nbf.v4.new_markdown_cell(
        "## 7. Next steps\n\n"
        "- Nothing here is final -- this is process prototyping, not the frozen T-033 pipeline.\n"
        "- Once Friday's meeting confirms region/horizon, rerun `fetch_hotspots.py`/`fetch_weather.py`/"
        "`fetch_landcover.py` against the confirmed scope and full 2000-2025 window.\n"
        "- Wind data source still needed (BOM or ERA5) -- SILO confirmed not to have it.\n"
        "- Land-cover sampling here used 500 of the widened window's unique locations for speed; "
        "the full pipeline will need every hotspot location, or a smarter spatial join."
    ))

    nb["cells"] = cells
    # Kaggle's execution runner (papermill) requires a kernelspec in notebook
    # metadata -- nbf.v4.new_notebook() leaves this empty. Missing it doesn't
    # break local nbconvert execution (more lenient), only Kaggle's, which is
    # exactly why this passed local checks but failed live (T-042).
    nb["metadata"] = {
        "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
        "language_info": {"name": "python"},
    }
    output_path.write_text(nbf.writes(nb))
    return output_path


def main() -> None:
    build_notebook(HERE / "active_fire_data_exploration.ipynb")


if __name__ == "__main__":
    main()
