# Agent instructions — 36127 Innovation Lab: Capstone Project

Scope: this file applies to work under this subject folder only (`llm-wiki/02-subjects/36127-innovation-lab-capstone-project/`), not the rest of the `uts-mdsi` repo.

Tuan is currently working **Project 15: Build a Custom Harness and Beat an Established One on Terminal-Bench**. Ignore the Project 14 preference in `assignments/group-formation-outreach-2026.md` — that was superseded once the group landed on Project 15.

## Start here

- [project-15/agent-collaboration-log.md](project-15/agent-collaboration-log.md) — running open discussion between Tuan and whichever AI tools he's using (Claude, Codex, Antigravity so far). Read the latest entries before starting work here, and append a new entry (don't edit past ones) when you make a notable decision, finding, or handoff. Sign entries with your actual tool name.
- [project-15/README.md](project-15/README.md) — project brief, workstreams, definition of done, evidence standard.
- [project-15/team-task-tracker.md](project-15/team-task-tracker.md) — milestones and the P15-### task register; update task status/evidence here, not in the collaboration log.
- [project-15/experiment-register.md](project-15/experiment-register.md) — record every smoke test, baseline run, or ablation here with full run metadata before interpreting results.
- [project-15/meeting-and-decision-log.md](project-15/meeting-and-decision-log.md) — formal team/mentor/client decisions only.

## Working conventions

- Task status, experiment results, and formal decisions belong in their dedicated files above, not in the collaboration log — the log is for open discussion, questions, and handoffs.
- Ground content in real sources (mentor notes, literature, actual run output); don't fabricate results or dates.
- **Distinguish stable knowledge from live/mutable state.** Academic papers, the official brief, and architecture principles don't go stale — check them once. Leaderboard rankings, current model lineups, pricing, and which harnesses a brief's example wording mentions all *do* go stale — re-check these against a live source at each real decision point (not just when someone asks), especially before P15-014/015 (Week 3 baseline freeze) and the Week 9 final-evaluation freeze. This rule exists because of two same-day incidents on 5 Aug 2026 (stale model names in a mentor agenda; an unverified harness recommendation inherited from the brief) — see `project-15/agent-collaboration-log.md` for the full incident notes.
- When picking up work, check `agent-collaboration-log.md` first for the latest context before re-deriving it.
- Weekly mentor-meeting agendas go in `project-15/week-<NN>-mentor-agenda-<YYYY-MM-DD>.md` (zero-padded week number, matching the task tracker's week numbering), linked from `project-15/README.md`'s "Weekly mentor-meeting agendas" section.
