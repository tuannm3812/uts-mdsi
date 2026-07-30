# Public Data Source Audit — Active-Fire Pilot

**Checked:** 30 July 2026

## Decision

The pilot can be run from public sources without a DEA secure account, FIRMS API key, or manual browser export.

## Sources

| Source | Public access confirmed | Relevant content | Licence/constraint | Pilot role |
|---|---|---|---|---|
| DEA Hotspots WFS | Yes | Historical point records; satellite, sensor, algorithm/version, acquisition time, temperature, power, confidence, state, and positional accuracy | CC BY 4.0; not for safety-of-life decisions | Primary hotspot observations |
| NSW Fire History Feature Service | Yes | Polygon geometry; fire ID/name/type; ignition, capture and extinguish dates; cause; area; agency | Public query/extract service | Complementary event reference |
| NPWS Fire History download/WFS | Yes | Wildfire and prescribed-burn final boundaries, monthly updates | CC Attribution | Alternative/reference-completeness check |
| Historical FESM | Yes | Retrospective fire extent and severity mapping | CC Attribution | Potential independent extent check |
| NSW RFS Current Incidents Feed | Yes for current feed | GeoJSON/GeoRSS/CAP incidents, nominal 30-minute updates | Public page does not establish historical archive access | Not usable for the 2019–20 retrospective pilot without an archive |
| NASA FIRMS | Yes, with its own access workflow | MODIS/VIIRS active-fire archive | Not independent from DEA records based on the same products | Source-product comparison, not ground truth |

## DEA access evidence

- WFS layer: `public:hotspots`
- Historical records reported by `resultType=hits` on 30 July 2026: approximately 94 million
- Pilot query format: WFS `GetFeature`, GeoJSON output, CQL date range and spatial `BBOX`
- Pilot fields observed: `id`, `satellite`, `sensor`, `process_algorithm`, `process_algorithm_version`, `product`, `longitude`, `latitude`, `temp_kelvin`, `power`, `confidence`, `datetime`, `australian_state`, and `accuracy`

## NSW Fire History access evidence

- ArcGIS layer: `NSWFireHistory/FeatureServer/0`
- Output used: GeoJSON in EPSG:4326
- Fields used: `fire_id`, `fire_name`, `fire_type`, `ignition_date`, `capture_date`, `extinguish_date`, `ignition_cause`, `capt_method`, `area_ha`, `perim_km`, `state`, and `agency`
- Event query requires interval-overlap logic. Filtering only on ignition dates incorrectly omits fires that began before the hotspot window.
- Open-ended records with missing extinguish dates require a bounded ignition lookback, otherwise unrelated historical events are returned.

## Pilot query

- Bounding box: `149.5,-33.7,151.0,-32.3` in WGS84
- Hotspots: `2020-01-01T00:00:00Z` to, but excluding, `2020-01-15T00:00:00Z`
- Fire-event ignition lookback: `2019-07-01`
- Fire-event interval condition: ignition before pilot end and extinguish on/after pilot start, or missing

## Manual action required

None for this pilot.

Possible later manual or supervisor-assisted access would be useful only if:

1. a historical archive of operational NSW RFS incidents is required;
2. a higher-precision active-flame reference exists internally;
3. secure DEA-only sources are scientifically necessary; or
4. Dr Arnick has an already curated event dataset that reduces label uncertainty.
