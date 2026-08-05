# Cost & Runtime Notes — Input for P15-011

Research notes for the cost model task (P15-011, owned by Faisal Shoaib, not yet started). Checked 5 Aug 2026 — see [leaderboard-snapshot-2026-08-05.md](leaderboard-snapshot-2026-08-05.md) for the underlying leaderboard data.

## Cost — real data available

Full 89-task run costs from the live leaderboard range **$134.09 to $2,059.19**, depending on model and reasoning effort. Our proposed model (Fable 5, per Q1) costs $552.67 (Claude Code) or $438.64 (Terminus 2) at "xhigh"/"high" effort.

**Open uncertainty, worth confirming with Will:** the lit review's "Leaderboard versus academic evaluation" section states official leaderboard submission requires at least 5 trials per task (≥445 runs). It's not confirmed whether the displayed leaderboard costs already reflect 5 trials, or just one. If they already include 5 trials, per-trial development cost is roughly 5× cheaper than the headline figures suggest — a big difference for planning the 20-task dev-subset budget.

## Runtime — not published, needs empirical measurement

Checked: tbench.ai's "How to run Terminal-Bench 2.1" docs, Harbor's own docs and GitHub README, and a third-party eval integration (EvalScope). **None publish a wall-clock duration for a full run.** What is confirmed:

- Harbor supports parallel execution via `--n-concurrent` (docs show example values of 4 and 8, no stated recommendation).
- Each task's agent timeout is configurable per-task via `[agent].timeout_sec` in that task's `task.toml` — no universal default found.
- Build-phase timeout is a fixed 600 seconds across all tasks.

**Do not use** the 69–93 min/task figure from Long-Horizon-Terminal-Bench (a different, deliberately harder 46-task derivative benchmark) as a TB2.1 estimate — it would overstate standard TB2.1 task duration.

**Recommendation:** P15-009 (oracle smoke test, 5 tasks, not yet started) is the team's own planned mechanism for getting a real number — run it before estimating full-run time, and extrapolate from the actual measured per-task duration × `89 / n_concurrent` rather than guessing.
