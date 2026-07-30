# Research Tooling and Reproducibility

## Principle

Use the smallest reliable stack that supports geospatial time-series research. Add specialised tools only after the task and dataset are fixed.

## Literature and evidence

| Need | Tool | Use |
|---|---|---|
| Reference library | Zotero | Store PDFs, metadata, tags, notes, and citation keys |
| Discovery | Scopus, Web of Science, Google Scholar, UTS Library | Run and document repeatable searches |
| Citation chaining | Semantic Scholar and Connected Papers | Find predecessors and related work; verify against publisher records |
| Screening | Spreadsheet or Rayyan | Record include/exclude decisions |
| Writing | Markdown initially; Quarto or LaTeX later | Keep prose and citations versionable |
| Bibliography | Better BibTeX for Zotero | Export stable BibTeX keys |

AI may assist with search-term expansion and synthesis, but each factual claim must be checked against the paper itself.

## Data engineering

- Python 3.11 where library compatibility permits
- `pandas` and `polars` for tabular processing
- `geopandas`, `shapely`, and `pyproj` for vector geospatial work
- `xarray`, `rioxarray`, and `rasterio` for gridded/raster data
- Parquet/GeoParquet for derived tables
- Zarr or NetCDF for chunked multidimensional arrays
- DuckDB for local analytical queries
- STAC clients or official APIs for remote-sensing catalogues

Raw and derived datasets should remain outside Git. Commit manifests, schemas, checksums, licences, and acquisition scripts.

## Modelling

### Baselines first

- Scikit-learn logistic regression
- Random forest
- XGBoost or LightGBM
- Optional recurrent baseline only if temporal sequences are central

### Advanced model after the decision gate

- PyTorch for neural modelling
- PyTorch Geometric for graph models
- A compact native PyTorch temporal transformer before adopting a larger framework

### Transparency and uncertainty

- SHAP for tree-based and model-agnostic feature attribution
- Captum for neural attribution where appropriate
- Calibration curves, Brier score, and temperature/isotonic calibration
- MAPIE or a small conformal-prediction implementation if conformal uncertainty matches the task
- Bootstrap or ensemble uncertainty as a robust baseline

## Experiment management

- Git for code, protocols, and small metadata
- Configuration files for every experiment
- Fixed random seeds with documented limitations
- MLflow locally if experiment volume justifies it; otherwise a structured results table
- `pytest` for data and leakage checks
- `ruff` for Python linting and formatting
- Environment lock file after the stack is confirmed

Every reported result must map to:

1. Git commit
2. Configuration
3. Data-manifest version
4. Random seed
5. Saved metrics
6. Model artefact or reproducible training command

## Compute strategy

| Stage | Environment |
|---|---|
| Literature, schemas, small data audits | Local machine |
| Feature-pipeline prototype | Local sample |
| Moderate tree baselines | Local or Kaggle CPU |
| Neural experiments | Kaggle GPU or Colab |
| Large geospatial preprocessing | Chunked local/cloud workflow; avoid loading full rasters into memory |

Do not select a model because cloud GPU is available. Estimate data volume and establish baseline difficulty first.

## Candidate public data sources

- NASA FIRMS standard science-quality MODIS/VIIRS active-fire archives for hotspot labels
- ERA5 or suitable Bureau of Meteorology products for weather and climate
- Digital Earth Australia land-cover and vegetation products
- Elevation and terrain products from Geoscience Australia
- Administrative regions or bioregions for spatial evaluation
- Road, population, and land-use layers only if their timestamps and licences are suitable

Dr Arnick has confirmed fire-hotspot detection and active-fire monitoring as the task, with a geographically broad review and a bounded Australian modelling case study. Dataset choice remains provisional until the monitoring definition and case-study region are selected.

## Suggested project layout

```text
research/
  research-execution-plan-2026.md
  tooling-and-reproducibility.md
sources/
  literature/
    literature-search-protocol.md
    literature-matrix.csv
    seed-literature-2026.md
notebooks/
  00_data_source_audit.ipynb
  01_baseline_exploration.ipynb
src/
  data/
  features/
  models/
  evaluation/
configs/
tests/
```

Notebooks are for exploration; reusable processing and modelling code should move into `src/`.
