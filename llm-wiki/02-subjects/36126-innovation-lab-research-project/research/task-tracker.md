# 36126 Research Project — Task Tracker

Task status lives here, not in the collaboration log. Formal decisions live in [decision-log.md](decision-log.md). Open discussion, review requests, and handoffs stay in [agent-collaboration-log.md](../agent-collaboration-log.md).

## How to use this tracker

- Update status here as work moves — don't rely on the collaboration log to reconstruct "what's done."
- Status vocabulary: **Not started** / **In progress** / **Blocked** / **Done** / **Paused (deliberate)**.
- Link the evidence (file, log entry, or external URL) for anything marked Done.
- This mirrors the phases already defined in [research-execution-plan-2026.md](research-execution-plan-2026.md) (decision gates G1–G6, semester phases 1–8); it doesn't replace that plan, it tracks progress against it.

## Phase 1 — Discovery (gap brief and supervisor-approved direction)

| ID | Task | Status | Evidence |
|---|---|---|---|
| T-001 | Literature search protocol and taxonomy | Done | `sources/literature/literature-search-protocol.md` |
| T-002 | Seed literature matrix (15 papers) | Done | `sources/literature/literature-matrix.csv` |
| T-003 | Citation verification against Crossref/arXiv | Done for the 11 papers cited in the sent brief (2 misattributions found and fixed); 3 uncited matrix rows (`Giglio2003MODIS`, `FireCluster2026`, `MTGFCI2026`) still unverified | Collaboration log, 2026-08-05 |
| T-004 | Data-feasibility pilot (NSW RFS source) | Done | `research/data-feasibility-pilot-2026-07-30.md`, `notebooks/active-fire-pilot/` |
| T-005 | Candidate gap formulation (A/B/C) | Done — Gap B recommended | D-006 in decision log |
| T-006 | Consolidated supervisor findings brief | Done | `research/supervisor-findings-brief-2026-08-03.md` |
| T-007 | Send brief to Dr Arnick | **Done** — sent 2026-08-03 | Collaboration log, 2026-08-05 (Tuan) |
| T-008 | Dr Arnick's response to the brief | **Done** — received 2026-08-05. Major direction correction, not a simple approval — reliability audit is Phase 1 groundwork, not the final contribution; real deliverable is a multimodal spatiotemporal transformer (MODIS FIRMS 2000–2025 + weather + land-cover/vegetation, cross-attention fusion) predicting either occurrence probability or 1–7 day hotspot forecasting, pick one | D-011 in decision log |
| T-009 | NPWS reference-source rerun and reconciled conclusion | Done | D-005, D-007 in decision log |
| T-010 | Follow-up message to Arnick (NPWS finding + citation correction) | Drafted, **not sent — deprioritised**. Arnick's reply moved past the reliability-audit specifics before this technical follow-up was sent; fold its content into the next reply instead of sending as a standalone message now | `communications/arnick-followup-npws-finding-2026-08-05.md` |
| T-030 | Decide Option A (occurrence-probability + explanation + spatial maps) vs Option B (1–7 day hotspot forecasting/nowcasting) — Arnick wants one, not both, due to semester timeframe | **Blocked — needs Tuan's decision**, see collaboration log for Claude's recommendation | D-011 |
| T-031 | Literature/methodology scan on multimodal spatiotemporal transformers for wildfire prediction — cross-attention fusion of satellite time series with weather/vegetation covariates, occurrence-probability vs short-horizon forecasting architectures, explainability/uncertainty methods for transformers. Arnick explicitly asked for this ("do a bit of search how this looks like... how to add innovation") | **Not started** — do after T-030 is decided, so the search is scoped to the right option | D-011 |
| T-032 | Evaluate the Digital Atlas of Australia "Bushfire Historical Extents" national dataset (all jurisdictions except NT, 1899–2024, harmonised burnt-area polygons) as an additional or replacement confidence-validation reference alongside NPWS/NSW RFS | **Not started** | Arnick's feedback, 2026-08-05 |
| T-033 | Source MODIS FIRMS hotspot time series 2000–2025 (full history, not just the Jan 2020 pilot window) and auxiliary weather (rainfall, temperature, wind, humidity) and land-cover/vegetation-condition datasets for the eventual case-study region | **Not started — depends on T-030** (case-study region/scope may narrow once the prediction option is fixed) | D-011 |

## Public Kaggle reproducibility pipeline

| ID | Task | Status | Evidence |
|---|---|---|---|
| T-011 | Notebook design (privacy, claims, reproducibility, visuals) | Done, reviewed, approved | D-003 |
| T-012 | Implementation plan (7 tasks) | Done, reviewed, approved | D-004 |
| T-013 | Task 1 — source-licence gate | Done | `notebooks/active-fire-kaggle/licence-manifest.json` |
| T-014 | Task 2–3 — deterministic analysis and visuals | Done | `notebooks/active-fire-kaggle/public_analysis.py`, `public_visuals.py` |
| T-015 | Task 4 — six-section notebook generation | Done | `notebooks/active-fire-kaggle/build_notebook.py` |
| T-016 | Task 5 — clean execution and privacy/claim audit | Done | `notebooks/active-fire-kaggle/audit_public_artifact.py` |
| T-017 | Task 6 — Kaggle metadata and credential-safe upload | Done | `notebooks/active-fire-kaggle/kaggle/`, `upload_private.py` |
| T-018 | Task 7 — Claude review gate and private deployment | Done — Version 10 live, private, CPU-only, internet-off, owner-only | Collaboration log, 2026-08-05 |
| T-019 | Public release of the Kaggle dataset/kernel | Done — Version 14 public. Tuan confirmed direct authorisation 2026-08-05 (D-010) | Kaggle Dataset & Kernel URLs, commit `2bdc352` / `539c33b`, D-010 |
| T-022 | Fix Cells 17 and 20 in the notebook: sensor-composition and per-sensor match-rate claims are factually wrong against the actual staged data (AHI is the dominant sensor at 68.9%, not VIIRS at "over 80%"; MODIS's real match rate is 99.0%, not the claimed 92.5%) | Done, verified independently | `build_notebook.py`, commit `539c33b`, Version 13 Kaggle push |
| T-023 | Expose spatiotemporal matching parameters in configuration blocks and group imports per master coding standards | Done | `build_notebook.py`, `build_eda_notebook.py`, commit `686f7eb` |
| T-024 | Enrich dataset-metadata.json (subtitle, description, resources) to resolve Kaggle usability checklist gaps | Done | `kaggle/dataset-metadata.json`, Version 13 Kaggle push |
| T-025 | Fix Cell 23's confidence-distribution takeaway — currently live and public. Claims MODIS median confidence is "around 67%" (actual median is 50.0; mean is 65.4) and that VIIRS is "a nominal class mapping (nominal/high)" (actually a mix of a 3-value-only algorithm, 76% of records, and a fully continuous one, 21%). Third instance of the same root cause as T-022 — hardcoded prose never cross-checked against the real data | Done | `build_notebook.py`, Version 15 Kaggle push |
| T-026 | Update `test_kernel_is_private_cpu_and_snapshot_first` and `test_dataset_is_private_and_has_no_collaborators` — both hardcode the pre-T-019 private-only assumption and now fail, not because of a regression but because they weren't updated when D-010 changed the intended state | Done | `tests/test_kaggle_metadata.py`, 20/20 green tests |
| T-027 | Structural fix: narrative takeaway text in `build_notebook.py` has now been wrong three separate times (T-022 x2, T-025) because it's hand-typed prose never checked against the computed dataframes. Consider generating these strings from the actual computed values, or adding a narrative-vs-data cross-check to `audit_public_artifact.py` | Done | Implemented dynamic python code takeaways using computed dataframe values in both build scripts, resolving stats drift permanently |
| T-028 | Fix `build_eda_notebook.py` lines 225 and 283 — the EDA notebook (`1_active_fire_eda.ipynb`, also live and public) has the same two error patterns as T-022/T-025 in a separate file: claims VIIRS is the dominant sensor (actually AHI, 68.9% vs 22.4%) and that VIIRS/MODIS confidence follows a clean discrete-vs-continuous split (it doesn't — see T-025 for the real per-algorithm breakdown) | Done | `build_eda_notebook.py`, Version 15 Kaggle push |
| T-029 | Fix Kaggle dataset Usability panel gaps (Source/Provenance ✗, Update Frequency ✗, File Description ✗ — screenshotted by Tuan). Root-caused via Kaggle's own schema docs: `dataset-metadata.json` uses the wrong key `updateFrequency` (should be `expectedUpdateFrequency` — Kaggle silently ignores the wrong key, so "never" has never actually applied); the dedicated `userSpecifiedSources` field is missing entirely (DEA/NPWS source info only exists in the free-text `description`, which doesn't satisfy this separate check). File Description cause unconfirmed — local `resources` array looks complete for all 7 uploaded files; needs checking against the live Kaggle page after redeploy, not just source | Done | `dataset-metadata.json` updated with correct schema keys, Version 16 Kaggle push |



## Repository hygiene

| ID | Task | Status | Evidence |
|---|---|---|---|
| T-020 | Stop tracking `output/`, `tmp/`, `__pycache__/` scratch files | Done | `.gitignore`, commit `d4014d3` |
| T-021 | Split collaboration log into log/tracker/decision-log | Done | D-009, this file |

## Phase 2 onward (unblocked as of D-011, not yet started)

Arnick's response (T-008/D-011) unblocks this, and also clarifies it: `research-execution-plan-2026.md`'s original Phase 5 ("Advanced model — Transformer or graph pipeline") and Phase 6 ("Trust analysis — explanation stability, calibration, uncertainty") were already the right shape for this — the project drifted toward treating Phase 1's reliability audit as the destination instead of a gate feeding those later phases. Immediate next steps, in order: T-030 (pick Option A/B) → T-031 (scoped literature/methodology scan) → T-032/T-033 (data sourcing) → protocol freeze (target dataset, split design, metrics) → baselines → the actual multimodal transformer. Detailed sub-tasks for baselines/advanced-model/trust-analysis/robustness/writing aren't worth writing yet until T-030 fixes the target.
