# Agent instructions — 36126 Innovation Lab: Research Project

Scope: this file applies to work under this subject folder only (`llm-wiki/02-subjects/36126-innovation-lab-research-project/`), not the rest of the `uts-mdsi` repo.

Tuan is researching transparent fire-hotspot detection and active-fire monitoring in NSW, supervised by Dr Arnick Abdollahi. The reliability/confidence-auditing work (Gap B, D-006/D-007) is **Phase 1 — a data-quality gate, not the destination** (Arnick's direction correction, D-011). The actual deliverable is a multimodal spatiotemporal transformer trained on a confidence-filtered MODIS FIRMS hotspot time series (2000–2025) fused with weather and land-cover/vegetation data, predicting **Option B: 1–7 day hotspot forecasting/nowcasting with confidence** (D-012). See `research/research-execution-plan-2026.md`'s "Arnick's 5 August direction" section for the current near-term sequencing.

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
