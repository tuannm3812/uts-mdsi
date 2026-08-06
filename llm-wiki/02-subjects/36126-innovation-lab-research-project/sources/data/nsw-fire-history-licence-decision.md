# NSW Fire History Licence Decision

**Checked Date:** 2026-08-04  
**Assessed Item:** NSW Fire History Feature Service (NSW RFS)  
**ArcGIS Item ID:** `99b11f8af9444737b3f484dd7334d671`  
**Official URL Checked:** [NSW ArcGIS Portal Item Metadata](https://portal.data.nsw.gov.au/arcgis/home/item.html?id=99b11f8af9444737b3f484dd7334d671)  

## Licence Assessment

- **Stated License Field:** The formal `licenseInfo` field in the ArcGIS metadata is completely empty.
- **Description Text:** The description field contains the text `Terms and Conditions: Creative Common`, but does not specify the version (e.g., CC BY 3.0, CC BY 4.0) or terms of attribution and redistribution.
- **Redistribution Status:** Due to the absence of a formal, unambiguous versioned Creative Commons license, we cannot legally redistribute raw records, geometry, or record-level derivatives of the NSW RFS dataset on a public platform (such as Kaggle).

## Alternative Source: NPWS Fire History

- **Source:** Data.NSW National Parks and Wildlife Service (NPWS) Fire History Dataset.
- **Stated License:** Explicitly licensed under Creative Commons Attribution (CC BY 4.0), allowing redistribution with proper attribution.
- **URL Checked:** [NPWS Fire History on Data.NSW](https://data.nsw.gov.au/data/dataset/fire-history-wildfires-and-prescribed-burns-1e8b6)

---

## Decision

**Selected Decision: Decision B**  
*NPWS replacement and full pilot rerun required.*

Since no authoritative exact licence is confirmed for the NSW RFS `NSWFireHistory/FeatureServer/0` layer, we prohibit its packaging. Instead, the public pilot notebook will use the NPWS Fire History dataset as the public reference source. The pilot execution will be rerun to compute a new set of baseline figures, invariants, maps, and interpretations.

---

## Implementation Details

The `licence-manifest.json` will register the confirmed sources:
1. **DEA Hotspots:** CC BY 4.0 (Attribution: Geoscience Australia)
2. **NPWS Fire History:** CC BY 4.0 (Attribution: NSW National Parks and Wildlife Service)
