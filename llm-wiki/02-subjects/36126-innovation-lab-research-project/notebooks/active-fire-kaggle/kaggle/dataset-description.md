# NSW Active-Fire Reliability Pilot Dataset

## Overview
This dataset contains a spatiotemporal snapshot of satellite-derived active-fire observations and historical fire boundaries in New South Wales (NSW), Australia. It is compiled specifically to support **calibration and spatiotemporal reliability auditing** of satellite hotspot products during a fortnight of intense fire activity in January 2020 (specifically covering the Gospers Mountain and Greater Blue Mountains fire periods).

## Data Sources & Licensing
This dataset is published under a Creative Commons Attribution 4.0 International License (CC BY 4.0).
* **DEA Hotspots WFS:** Provided by Geoscience Australia under CC BY 4.0. Service URL: [DEA Hotspots Service](https://hotspots.dea.ga.gov.au/)
* **NPWS Fire History:** Provided by NSW National Parks and Wildlife Service under Creative Commons Attribution. Dataset URL: [Data.NSW NPWS Record](https://data.nsw.gov.au/data/dataset/npws-fire-history)

## Files
1. **`dea_hotspots.geojson`**: A point layer containing satellite hotspot observations. Properties include acquisition timestamps, coordinates, sensor names (MODIS, VIIRS, AHI), processing algorithms, and confidence metrics.
2. **`npws_fire_history.geojson`**: A polygon boundary layer containing fire complexes managed by the NSW National Parks and Wildlife Service. Properties include fire names, starting/ignition dates, end/extinguishment dates, and fire type classifications (e.g. bushfire vs. prescribed burn).
3. **`snapshot-manifest.json`**: Explicit provenance metadata, including SHA-256 checksums and dataset origins, ensuring reproducibility.

## Intended Use
This snapshot is designed for educational and academic research. It provides a benchmark for testing spatiotemporal matching algorithms and analyzing the challenges of event-level validation when target reference boundaries are represented as consolidated, whole-of-season fire complexes.
