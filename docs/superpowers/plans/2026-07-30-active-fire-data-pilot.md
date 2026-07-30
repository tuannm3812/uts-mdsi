# Active-Fire Data Pilot Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Determine whether public DEA hotspot and NSW fire-event data can support a reproducible active-fire reliability study without supervisor-provided data.

**Architecture:** A standard-library Python pipeline will retrieve a bounded public sample, normalize hotspot points and NSW fire polygons, match observations by space and time, and emit auditable CSV/JSON summaries. Network retrieval is separated from deterministic matching so tests use small fixtures and the analysis can be rerun without repeated downloads.

**Tech Stack:** Python 3 standard library, `pytest`, public HTTP/ArcGIS/WFS/AWS endpoints, CSV, GeoJSON, Markdown.

## Global Constraints

- Primary research task is hotspot detection and active-fire monitoring, not fire spread.
- Start with a bounded NSW case study and one fire season.
- Do not treat satellite-product agreement as independent ground truth.
- Preserve raw downloads and record source URLs, retrieval times, licences, and checksums.
- Do not commit large raw data; store reproducible small outputs and documentation in the repository.
- Do not require user action unless access requires authentication, licence acceptance, or a private archive.

---

### Task 1: Public-access and schema audit

**Files:**
- Create: `llm-wiki/02-subjects/36126-innovation-lab-research-project/sources/data/data-source-audit-2026-07-30.md`

**Interfaces:**
- Consumes: Official DEA and NSW endpoint metadata.
- Produces: Chosen pilot region/time window, endpoint inventory, and documented access blockers.

- [ ] **Step 1:** Inspect DEA AWS, WFS, GeoJSON, and document endpoints without authentication.
- [ ] **Step 2:** Inspect the NSW Fire History ArcGIS schema and query/count support.
- [ ] **Step 3:** Select a pilot window with known NSW fire activity and manageable data volume.
- [ ] **Step 4:** Record source, access method, licence, temporal fields, geometry, and independence limitations.

### Task 2: Matching-core tests

**Files:**
- Create: `llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-pilot/tests/test_match_hotspots.py`
- Create: `llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-pilot/tests/fixtures/fire_polygons.geojson`
- Create: `llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-pilot/tests/fixtures/hotspots.csv`

**Interfaces:**
- Consumes: Normalized hotspot dictionaries and GeoJSON Polygon/MultiPolygon features.
- Produces: Failing behavioral tests for `point_in_geometry`, `within_event_window`, and `classify_hotspot`.

- [ ] **Step 1:** Write tests for points inside, outside, and on polygon boundaries.
- [ ] **Step 2:** Write tests for MultiPolygon geometry.
- [ ] **Step 3:** Write tests for ignition/extinguish windows and missing dates.
- [ ] **Step 4:** Write tests distinguishing bushfire, prescribed burn, and unmatched observations.
- [ ] **Step 5:** Run `pytest` and confirm failure because the matching module does not yet exist.

### Task 3: Deterministic matching implementation

**Files:**
- Create: `llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-pilot/match_hotspots.py`

**Interfaces:**
- Produces:
  - `point_in_geometry(lon: float, lat: float, geometry: dict) -> bool`
  - `within_event_window(observed_at: datetime, properties: dict, grace_days: int) -> bool`
  - `classify_hotspot(hotspot: dict, features: list[dict], grace_days: int) -> dict`

- [ ] **Step 1:** Implement Polygon and MultiPolygon point containment including boundary handling.
- [ ] **Step 2:** Implement UTC date parsing and event-window checks.
- [ ] **Step 3:** Implement deterministic classification and matching metadata.
- [ ] **Step 4:** Run the targeted tests and confirm they pass.

### Task 4: Reproducible public-data retrieval

**Files:**
- Create: `llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-pilot/fetch_public_data.py`
- Create: `llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-pilot/tests/test_fetch_public_data.py`
- Create: `llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-pilot/source-config.json`

**Interfaces:**
- Produces raw source files plus `provenance.json` with URLs, retrieval timestamps, byte sizes, and SHA-256 checksums.

- [ ] **Step 1:** Write failing tests for URL construction, pagination, and provenance hashing.
- [ ] **Step 2:** Implement ArcGIS pagination and bounded hotspot retrieval using the confirmed public access route.
- [ ] **Step 3:** Download a bounded pilot sample to a temporary/raw-data location.
- [ ] **Step 4:** Validate HTTP status, content type, record count, geometry, and required fields.
- [ ] **Step 5:** Run retrieval tests and confirm they pass.

### Task 5: Pilot analysis and feasibility report

**Files:**
- Create: `llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-pilot/run_pilot.py`
- Create: `llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-pilot/README.md`
- Create: `llm-wiki/02-subjects/36126-innovation-lab-research-project/research/data-feasibility-pilot-2026-07-30.md`
- Create: `llm-wiki/02-subjects/36126-innovation-lab-research-project/research/data-feasibility-pilot-results.csv`

**Interfaces:**
- Consumes: Retrieved hotspot records and NSW fire polygons.
- Produces: Counts, missingness, match classes, sensitivity across spatial/temporal tolerances, and a go/modify/stop recommendation.

- [ ] **Step 1:** Normalize fields and profile missingness.
- [ ] **Step 2:** Match hotspots to event polygons and event windows.
- [ ] **Step 3:** Separate bushfire, prescribed-burn, spatial-only, temporal-only, and unmatched cases.
- [ ] **Step 4:** Run sensitivity checks for documented sensor-position and time tolerances.
- [ ] **Step 5:** Write the feasibility report, limitations, and precise supervisor questions.
- [ ] **Step 6:** Copy the report and compact outputs to the organized Google Drive research folder.

### Task 6: Verification

**Files:**
- Modify: `llm-wiki/02-subjects/36126-innovation-lab-research-project/README.md`

- [ ] **Step 1:** Run the complete pilot test suite.
- [ ] **Step 2:** Rerun the pipeline from saved raw inputs and compare output checksums.
- [ ] **Step 3:** Confirm source counts, date ranges, CRS, and matching classes against raw records.
- [ ] **Step 4:** Run `git diff --check`.
- [ ] **Step 5:** Verify Google Drive copies byte-for-byte.
- [ ] **Step 6:** Report any access that still requires the user or supervisor.
