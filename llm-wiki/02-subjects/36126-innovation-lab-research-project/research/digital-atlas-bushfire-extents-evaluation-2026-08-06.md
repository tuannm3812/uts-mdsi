# T-032 — Digital Atlas of Australia "Bushfire Historical Extents" Evaluation

**Purpose:** Arnick explicitly named this dataset (`digital.atlas.gov.au/datasets/524e2962...`) in his 5 August message as a candidate confidence-validation reference. Evaluated its metadata against what the reliability-audit pipeline already uses (NPWS Fire History, NSW RFS) before the Friday meeting, per open question 4 in the [meeting-prep doc](../assignments/week-02-mentor-meeting-prep-2026-08-07.md).

**Method:** metadata review only (license, coverage, format, lineage), via the Geoscience Australia catalogue record. Did not download or process the 775.7MB geodatabase — not feasible before Friday, and not necessary to answer the licensing/lineage question.

## Findings

- **Full name:** Bushfire Historical Extents — Version 3.0. Published by Geoscience Australia under the National Bushfire Intelligence Capability (a partnership between Australian Climate Services, CSIRO, GA, and EMSINA).
- **Coverage:** all Australian states/territories except the Northern Territory; 1899-12-30 to 2024-08-29.
- **License: Creative Commons Attribution 4.0 International (CC BY 4.0)**, © Commonwealth of Australia (Geoscience Australia) 2024 — explicitly and unambiguously redistributable, same licence class as NPWS Fire History (D-005). Not a licensing blocker either way.
- **Format:** File Geodatabase, GDA94 geographic (EPSG:4283), 775.7MB zipped.
- **Update frequency:** "Not planned" — minor updates only through 30 June 2025, otherwise a static historical snapshot.
- **Lineage — the important part:** it's an aggregation of **jurisdictional-supplied** burnt-area polygons, standardised to a common national data dictionary. For NSW specifically, the catalogue lineage names **New South Wales Parks and Wildlife** as the contributing source — the same agency behind NPWS Fire History, which is already the reliability pipeline's broad/complex-level reference (D-005, D-007).

## Implication for open question 4

This is very likely **not an independent reference for NSW** — it appears to be the same underlying NSW data, re-aggregated nationally, not a different-granularity source that would fix the mega-complex-dominance problem already found (Kerry Ridge/Gospers Mountain ≈98% of matches, D-007). If that's right, using it alongside NPWS for NSW confidence-filtering would double-count the same source rather than triangulate two independent ones.

**Caveat:** this is inferred from catalogue-level lineage metadata, not verified by pulling the actual NSW records out of the geodatabase and comparing them feature-by-feature against the NPWS layer already processed. That comparison is doable but not before Friday (775MB download + geometry diffing).

**Recommendation to bring to the meeting:** don't treat it as a replacement or a second independent reference for NSW. It's genuinely useful for one thing NPWS/RFS can't do alone — **cross-jurisdictional coverage**, if the case-study region ends up spanning a state border or if Arnick wants a national comparison point later. Worth confirming directly with him rather than assuming, since he raised it — but the working answer is "supplementary, not a fix for the granularity problem," pending the feature-level check if it turns out to matter.
