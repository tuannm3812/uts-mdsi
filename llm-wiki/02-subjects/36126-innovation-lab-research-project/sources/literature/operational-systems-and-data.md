# Operational Systems and Data Sources

## Digital Earth Australia Hotspots

- **Provider:** Geoscience Australia / Digital Earth Australia
- **Role:** National bushfire hotspot monitoring and historical data service
- **Coverage:** 27 August 2002 to present
- **Update frequency:** Every 10 minutes
- **Spatial form:** Vector hotspot records
- **Licence:** Creative Commons Attribution 4.0
- **Sensors:** MODIS, VIIRS, and Himawari/AHI among current documented sources
- **Access:** Map, downloads, AWS, WMS, WFS, KML, and GeoJSON
- **Relevant fields:** Sensor, acquisition time, processing time, algorithm/version, temperature, power, confidence, state, and positional accuracy

### Documented limitations

- False positives and false negatives occur.
- Hotspots may represent industrial heat, furnaces, smoke plumes, contrails, or hot rocks rather than bushfires.
- Location accuracy is ±375 m at best.
- Geostationary detections have unreliable periods around sunrise and sunset.
- Cloud, smoke, canopy, small footprint, cool fires, sensor outages, and overpass timing can produce missing detections.
- The service is not intended to be used alone for safety-of-life decisions.

Sources:

- [DEA overview](https://www.ga.gov.au/scientific-topics/dea/dea-data-and-products/dea-hotspots)
- [Technical product documentation](https://knowledge.dea.ga.gov.au/data/product/dea-hotspots/)

## MyFireWatch

- **Provider:** Landgate
- **Role:** Public Australian hotspot and fire-context map
- **Layers:** Recent hotspots, fire-danger ratings, forecast wind, vegetation greenness, burnt areas, and lightning
- **Hotspot windows:** 0–12, 12–24, 24–48, and 48–72 hours
- **Typical update:** Every two to four hours, subject to satellite availability

### Documented limitations

- Not intended for decisions about active fires or preservation of life/property.
- Small, cool, canopy-obscured, cloud-obscured, or smoke-obscured fires may be missed.
- Hotspots may be non-fire heat sources such as heavy industry.
- Approximate location accuracy is within 2 km and may reach 5 km near image edges.
- It does not differentiate prescribed burns from bushfires.

Sources:

- [MyFireWatch map](https://myfirewatch.landgate.wa.gov.au/map.html)
- [About](https://myfirewatch.landgate.wa.gov.au/about.html)
- [Usage and limitations](https://myfirewatch.landgate.wa.gov.au/help.html)

## European Forest Fire Information System

- **Provider:** Copernicus Emergency Management Service
- **Role:** European and global active-fire visualization using NASA FIRMS thermal-anomaly detections
- **Sensors described:** MODIS at approximately 1 km and VIIRS at 375 m
- **Typical availability:** Approximately two to three hours after satellite acquisition
- **Typical update:** Six times per day
- **Filtering:** A knowledge-based filter considers surrounding land cover, distance to urban or artificial surfaces, and the source-product confidence

### Documented limitations

- A hotspot is a thermal anomaly, not proof of a vegetation fire.
- Detection location is constrained by sensor resolution and geolocation accuracy.
- Small fires and fires obscured by cloud, smoke, or vegetation may be missed.
- Other heat sources may be detected as fires.
- Higher VIIRS spatial resolution improves detection of relatively small fires, but does not remove these observation limitations.

Source:

- [EFFIS active-fire detection technical background](https://forest-fire.emergency.copernicus.eu/about-effis/technical-background/active-fire-detection)

## Research implication

The project should not attempt to reproduce these operational maps. A stronger research contribution is to evaluate or improve the reliability of existing multi-sensor hotspot evidence for a bounded NSW case study.

Candidate targets include:

1. calibration of existing hotspot confidence against independently recorded fire events;
2. event-level consolidation of repeated multi-sensor detections;
3. classification and explanation of common false-alarm conditions;
4. robustness across sensors, seasons, subregions, and missing-observation conditions; and
5. comparison of existing confidence with a sensor-aware spatiotemporal reliability model.

The principal feasibility risk is constructing an independent and temporally accurate reference label from NSW incident or fire-history records.

EFFIS also changes the novelty threshold: knowledge-based false-positive filtering using land cover, urban proximity, and confidence already exists operationally. The research contribution must therefore be an evaluated improvement—for example calibration, event-level fusion, geographic robustness, or explanation quality—rather than simply adding contextual filters.
