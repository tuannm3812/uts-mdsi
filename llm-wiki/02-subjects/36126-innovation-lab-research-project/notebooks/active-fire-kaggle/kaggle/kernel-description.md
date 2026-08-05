# NSW Active-Fire Reliability Pilot

## Analysis Overview
This notebook executes a spatiotemporal reliability audit matching satellite hotspot observations (DEA Hotspots) against official post-event fire boundary records (NPWS Fire History) in New South Wales (NSW), Australia. 

It evaluates matching performance under two regimes:
1. **Exact Spatial Matching (Baseline)**: Hotspot point must lie exactly inside the fire boundary polygon during the active burn period.
2. **Sensor-Buffered Matching**: Incorporates spatial buffers corresponding to each sensor's nominal resolution ($\epsilon_{\text{VIIRS}} = 0.375\text{ km}$, $\epsilon_{\text{MODIS}} = 1.0\text{ km}$, $\epsilon_{\text{AHI}} = 2.0\text{ km}$) and a temporal grace window ($\Delta t = 1\text{ day}$).

## Key Scientific Findings
* **Event Concentration Confound**: Out of 14 fire boundary events, **two mega-complexes (Gospers Mountain and Kerry Ridge) account for 97.85% of all matched hotspots**.
* **Scale Footprint Discrepancy**: Switching from NSW RFS (incident-level) to NPWS (consolidated whole-of-season complex boundaries) shifted matched hotspots from 17.1% to 97.12%. This jump is driven by the spatial scale of these mega-complexes rather than representing an increase in point-level sensor reliability.
* **Evaluation Caveat**: Due to the severe geographic concentration, model evaluations must implement **split-complex cross-validation** to prevent overfitting to the coordinates of the Blue Mountains/Gospers Mountain region.

## Reproducibility
All package pins are managed via `requirements-public.txt` and verified under CPU-only, internet-off constraints. Check the JSON reproducibility snapshot printed in the final cell of the notebook for exact shape and metric telemetry.
