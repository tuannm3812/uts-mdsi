# Decision Checklist — Friday 7 August Meeting

One page per decision. Tick the option Arnick actually chooses live during the call (PDF annotation — mark, highlight, or circle). Our recommendation is marked **(Recommended)**; if he picks something else, use the notes line. Full reasoning behind each recommendation is in [`week-02-mentor-meeting-prep-2026-08-07.md`](week-02-mentor-meeting-prep-2026-08-07.md) and the [speaking script](week-02-meeting-presentation-script-2026-08-07.md).

---

## 1. Forecast horizon

- ☐ Multi-horizon output across the full 1–7 days **(Recommended)**
- ☐ Single fixed horizon — specify: ..........................
- ☐ Something else — specify: ..........................

Notes: ..............................................................

---

## 2. Case-study region

- ☐ Widen to all of NSW **(Recommended)**
- ☐ A different fire-prone NSW subregion — specify: ..........................
- ☐ Keep the exact Greater Blue Mountains pilot footprint (despite the mega-complex concentration risk)
- ☐ Arnick has a specific preferred region — specify: ..........................

Notes: ..............................................................

---

## 3. Auxiliary data sources

- ☐ SILO (weather) + DEA Land Cover **(Recommended)**
- ☐ BOM instead of SILO for weather
- ☐ Arnick has a preferred/prepared dataset already — specify: ..........................
- ☐ Something else — specify: ..........................

Notes (wind is not available from SILO — confirmed; needs BOM or ERA5 separately, flag if this matters to him): ..............................................................

---

## 4. Digital Atlas "Bushfire Historical Extents" dataset — role

- ☐ Supplementary only (cross-jurisdictional use if region spans a state border), not a replacement for NPWS/RFS **(Recommended)**
- ☐ Treat as the primary/replacement reference instead of NPWS
- ☐ Worth doing the full feature-level verification (download + compare against NPWS directly) before deciding
- ☐ Something else — specify: ..........................

Notes: ..............................................................

---

## 5. Compute

- ☐ Kaggle free tier as default; escalate only if needed **(Recommended)**
- ☐ UTS-provided compute is available — specify: ..........................
- ☐ Cloud credits available (Colab Pro / GCP / other) — specify: ..........................
- ☐ Unknown — need to check and follow up

Notes: ..............................................................

---

## 6. Contribution framing

- ☐ "Reliability-aware forecasting" — label-confidence propagation + split-complex validation as contributions in their own right, alongside the model **(Recommended)**
- ☐ Model architecture/performance is the primary contribution
- ☐ Trust/explanation/uncertainty layer is the primary contribution
- ☐ Something else — specify: ..........................

Notes: ..............................................................

---

## 7. Cross-sensor matching (MODIS vs. VIIRS/Himawari agreement)

*Gap found on re-reading his message — not previously actioned.*

- ☐ Add as an explicit step within T-033 (data-foundation work) **(Recommended)**
- ☐ Not necessary — existing reference-boundary matching is sufficient
- ☐ Defer to a later phase (Phase 6, trust analysis)
- ☐ Something else — specify: ..........................

Notes: ..............................................................

---

## Summary — what I'm taking away (fill in during Section 5, "Close")

1. Horizon: ..............................................................
2. Region: ..............................................................
3. Auxiliary data: ..............................................................
4. Digital Atlas role: ..............................................................
5. Compute: ..............................................................
6. Contribution framing: ..............................................................
7. Cross-sensor matching: ..............................................................
