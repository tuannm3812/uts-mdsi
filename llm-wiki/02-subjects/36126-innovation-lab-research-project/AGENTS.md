# Agent instructions — 36126 Innovation Lab: Research Project

Scope: this file applies to work under this subject folder only (`llm-wiki/02-subjects/36126-innovation-lab-research-project/`), not the rest of the `uts-mdsi` repo.

Tuan is researching transparent fire-hotspot detection and active-fire monitoring in NSW, supervised by Dr Arnick Abdollahi. The reliability/confidence-auditing work (Gap B, D-006/D-007) is **Phase 1 — a data-quality gate, not the destination** (Arnick's direction correction, D-011). The actual deliverable predicts **fire-occurrence probability with uncertainty and transparent factor explanation** (D-014, 2026-08-07, confirmed live via the full Week 2 meeting transcript — supersedes D-012's earlier 1-7-day-forecasting pick), specifically:
- A **non-time-series, multimodal ML/DL model** (not a transformer — Arnick explicitly ruled out time-series modelling given only 2 years of audited data, T-033's full 2000-2025 FIRMS history is downgraded to optional/stretch, not a prerequisite).
- Built on the **existing ~15,000-record 2019-20 reliability-audited pilot data** (NSW Black Summer), **kept** as the case study — do not widen to all of NSW or a different subregion, that recommendation was explicitly reversed live.
- Via **fine-tuning an existing geospatial foundation model** (AlphaEarth/Satellite Embedding V1, Prithvi-EO-2.0) plus a genuine custom fusion mechanism (attention or similar), with baseline-model comparisons.
- Feeding toward an actual paper — Arnick outlined a full paper structure live, with journal submission as a stated possibility.

See `research/research-execution-plan-2026.md`'s "D-014 update" section for the full breakdown and near-term task sequence (T-049 through T-055).

## Start here, in this order

1. [research/task-tracker.md](research/task-tracker.md) — what's done, what's blocked, what's not started. Check this first, before re-deriving status from the collaboration log.
2. [research/decision-log.md](research/decision-log.md) — settled decisions with rationale. If you're about to propose something that contradicts a row here, read the rationale first; don't silently re-litigate it.
3. [agent-collaboration-log.md](agent-collaboration-log.md) — open running discussion between Tuan, Claude, and Codex/Antigravity. Read the latest entries for context and handoffs, and append a new entry (don't edit past ones) for notable findings, reviews, or decisions in progress.
4. [research/research-execution-plan-2026.md](research/research-execution-plan-2026.md) — the semester-level research plan (decision gates G1–G6, phases 1–8) that the task tracker tracks progress against.

## Working conventions

- Task status and formal decisions belong in `task-tracker.md` and `decision-log.md`, not in the collaboration log — the log is for open discussion, review requests, and handoffs.
- When a discussion in the log resolves into a settled decision or a task reaching Done, record it in the tracker/decision-log before moving on — don't leave it only in the log where the next session has to reconstruct it.
- Ground content in real sources (supervisor notes, literature, actual pilot/notebook output); don't fabricate results, dates, or citations. Citation attribution has been wrong before in this project (see decision log / task tracker T-003) — verify author names against Crossref/arXiv/publisher records before citing anything externally, don't just trust what's already written here.
- Everything supervision-related (Dr Arnick's name, messages, internal planning, draft outreach) must stay out of any public-facing artifact (the Kaggle notebook, its dataset, its landing pages). See the design spec in `docs/superpowers/specs/` and the privacy audit in `notebooks/active-fire-kaggle/audit_public_artifact.py` for what that boundary covers.
- The public Kaggle dataset/kernel stays private until Tuan explicitly authorises publishing (decision log D-008). Don't change visibility without that explicit instruction.
