---
type: source-capture
status: verbatim
---
# Project 15 — Official Brief (Verbatim)

**Source:** `01 Topic Lists/36127-capstone-project-list-spring-2026.pdf`, Project #15 entry (page containing "Project #15: Dr William So (Synogize)"). This is the **28 July 2026 revision** of the official Capstone project list — the one that added Projects 15 and 16 — downloaded to Google Drive on 28 Jul 2026. Extracted with `pdftotext -layout` on 4 Aug 2026. Full raw extraction of the whole 16-project document (all projects, not just 15) is at [../sources/raw/36127-capstone-project-list-spring-2026.txt](../sources/raw/36127-capstone-project-list-spring-2026.txt).

This is the authoritative source text. Every other Project 15 document in this repo (literature review, team task tracker, README) that describes the brief is a paraphrase or interpretation — cross-check against this file, not the other way around.

---

## Project #15: Dr William So (Synogize)

### Title

Build a Custom Harness and Beat an Established One on Terminal-Bench

### Project Description

Terminal-Bench 2.1 is a public benchmark of 89 terminal tasks with a leaderboard of harness + model pairs (tbench.ai). The same model scores very differently depending on the harness. Build a custom harness and get it to beat at least one established harness on the leaderboard tasks, with the model held constant.

### Why

- The harness, not just the model, now drives agent performance: the same model scores up to 16 points apart on Terminal-Bench depending only on the harness.
- Nobody has clean data on which harness design choices cause that gap. This project isolates them.
- Every team building agents faces the same build vs adopt decision. This produces evidence for it.

### Scope

- One benchmark (Terminal-Bench 2.1), one model held constant, two established harnesses for comparison.
- Iterate on a fixed dev subset of 20 tasks; run the full 89 only for final scoring.
- Build the minimum harness that runs the tasks, not a general framework.
- No fine-tuning, no comparing models, no writing new benchmark tasks.

### Objectives

- Set up Harbor (the open-source framework Terminal-Bench runs on) and run the 89 tasks through two established harnesses (e.g. Claude Code, OpenHands) using the same model, to reproduce the harness gap.
- Build a custom harness and plug it into Harbor as a custom agent.
- Iterate on one design lever at a time (system prompt, tools, context management, retries) against the 20-task dev subset until it beats an established harness there, then confirm on the full 89.
- Record accuracy, tokens and cost for every run.

### Expected outcomes

- A score table: custom harness vs established harnesses, same model, same 89 tasks.
- The harness repo plus a changelog showing which design changes moved the score.
- A submission of the custom harness to the public tbench.ai leaderboard.

---

## Notes for cross-checking other Project 15 documents

- **"16 points" gap** — the [literature review](../research/project-15-terminal-bench-literature-review.md)'s "16 percentage points" framing matches this verbatim text exactly.
- **New detail not previously captured anywhere in this repo:** the brief itself suggests **Claude Code and OpenHands** as example established harnesses ("e.g."). This is a suggestion in the brief, not a mandate — [team-task-tracker.md](team-task-tracker.md) P15-014/P15-015 (pin harness A/B) and [README.md](README.md)'s "Established harnesses: awaiting mentor/client confirmation" line should still get explicit mentor confirmation before treating this as fixed, but it's a strong starting proposal to raise with William Feng.
- **Adjacent brief for context:** Project #16 ("Build a Meta-Harness That Routes Terminal-Bench Tasks to the Best Harness," also Dr William So/Synogize) names three example harnesses — **Claude Code, OpenHands, Codex CLI** — and states it is "fully standalone" from Project 15/does not depend on it, though baseline runs could be shared if both projects are active. Relevant if "Team iLab 15-2" (seen in the mentor's Teams message) turns out to actually be a Project 16 team, or if there's any cross-team baseline-sharing opportunity worth raising with the mentor. Full Project 16 text is in the raw extraction linked above.
