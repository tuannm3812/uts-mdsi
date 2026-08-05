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
| T-008 | Dr Arnick's response to the brief | **Blocked — waiting on Arnick** | — |
| T-009 | NPWS reference-source rerun and reconciled conclusion | Done | D-005, D-007 in decision log |
| T-010 | Follow-up message to Arnick (NPWS finding + citation correction) | Drafted, **not sent** — hold until Arnick responds to T-007 | `communications/arnick-followup-npws-finding-2026-08-05.md` |

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
| T-019 | Public release of the Kaggle dataset/kernel | **Paused (deliberate)** — pending Tuan's explicit go-ahead | D-008 |
| T-022 | Fix Cells 17 and 20 in the notebook: sensor-composition and per-sensor match-rate claims are factually wrong against the actual staged data (AHI is the dominant sensor at 68.9%, not VIIRS at "over 80%"; MODIS's real match rate is 99.0%, not the claimed 92.5%) | Done | `build_notebook.py`, commit `539c33b`, Version 13 Kaggle push |
| T-023 | Expose spatiotemporal matching parameters in configuration blocks and group imports per master coding standards | Done | `build_notebook.py`, `build_eda_notebook.py`, commit `686f7eb` |
| T-024 | Enrich dataset-metadata.json (subtitle, description, resources) to resolve Kaggle usability checklist gaps | Done | `kaggle/dataset-metadata.json`, Version 13 Kaggle push |


## Repository hygiene

| ID | Task | Status | Evidence |
|---|---|---|---|
| T-020 | Stop tracking `output/`, `tmp/`, `__pycache__/` scratch files | Done | `.gitignore`, commit `d4014d3` |
| T-021 | Split collaboration log into log/tracker/decision-log | Done | D-009, this file |

## Phase 2 onward (not started)

Protocol freeze, data foundation, baselines, advanced model, trust analysis, robustness, and writing (phases 2–8 of `research-execution-plan-2026.md`) are all **Not started** — they depend on Dr Arnick's response to T-007/T-008 before scope can be frozen. No point tracking sub-tasks for these until that gate clears.
