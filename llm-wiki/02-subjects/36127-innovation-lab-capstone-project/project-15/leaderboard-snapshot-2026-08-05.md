---
type: source-capture
status: live-snapshot
---
# Terminal-Bench 2.1 Leaderboard — Snapshot 2026-08-05

**Source:** https://www.tbench.ai/leaderboard/terminal-bench/2.1, fetched via WebFetch (page-summarized, not read directly — cross-checked across three separate fetches for consistency). 17 total entries at time of capture.

This is a point-in-time snapshot, not a living document — per the live-source-recheck rule in `team-task-tracker.md` and `AGENTS.md`, take a fresh one before the Week 3 baseline freeze (P15-014/015) and again before the Week 9 final-evaluation freeze, rather than trusting this file to still be current by then. Name future snapshots `leaderboard-snapshot-<YYYY-MM-DD>.md`.

## Full table

| Rank | Agent | Model | Provider | Accuracy | Cost | Effort | Hacks | Date |
|---|---|---|---|---|---|---|---|---|
| 1 | Claude Code | Fable 5 | Anthropic | 83.8% ± 1.2% | $552.67 | xhigh | -0.2% | 7 Jun 2026 |
| 2 | Codex | GPT-5.5 | OpenAI | 83.1% ± 1.1% | $2,059.19 | xhigh | -0.2% | 1 May 2026 |
| 3 | Terminus 2 | Fable 5 | Anthropic | 80.4% ± 1.2% | $438.64 | high | -0.0% | 5 Jun 2026 |
| 4 | Cursor CLI | Grok 4.5 | xAI | 79.3% ± 1.5% | $134.09 | high | **-9.0%** | 9 Jul 2026 |
| 5 | Claude Code | Opus 4.8 | Anthropic | 78.9% ± 1.3% | $286.94 | high | -0.0% | 9 Jul 2026 |
| 6 | Codex | GPT-5.6 Terra | OpenAI | 78.4% ± 1.3% | $421.15 | max | -0.2% | 11 Jul 2026 |
| 7 | Terminus 2 | GPT-5.5 | OpenAI | 78.0% ± 1.2% | $493.85 | xhigh | -0.2% | 1 May 2026 |
| 8 | mini-SWE-agent | Muse Spark 1.1 | Meta | 76.2% ± 1.2% | $198.05 | xhigh | -0.0% | 9 Jul 2026 |
| 9 | Codex | GPT-5.6 Luna | OpenAI | 75.7% ± 1.3% | $241.45 | max | -0.9% | 11 Jul 2026 |
| 10 | Claude Code | Sonnet 5 | Anthropic | 74.6% ± 1.6% | $288.18 | high | -0.7% | 9 Jul 2026 |
| 11 | Terminus 2 | Gemini 3 Pro | Google | 73.9% ± 1.3% | $224.44 | high | -0.5% | 1 May 2026 |
| 12 | Claude Code | Opus 4.7 | Anthropic | 68.9% ± 1.4% | $599.52 | max | -0.5% | 1 May 2026 |
| 13 | Terminus 2 | Opus 4.7 | Anthropic | 66.1% ± 1.4% | $582.26 | max | -0.0% | 1 May 2026 |
| 14 | Gemini CLI | Gemini 3 Pro | Google | 65.8% ± 1.4% | $247.76 | high | -0.5% | 1 May 2026 |
| 14 | Gemini CLI | Gemini 3.1 Pro | Google | 65.8% ± 1.7% | $236.49 | high | -0.2% | 5 May 2026 |
| 16 | Terminus 2 | Gemini 3.1 Pro | Google | 65.6% ± 1.7% | $229.99 | high | -0.5% | 5 May 2026 |
| 17 | Claude Code | GLM-5.1 | Zhipu | 58.7% ± 1.2% | $277.14 | max | -0.0% | 1 May 2026 |

The page gives no description of what "Hacks" measures — inferred from the lit review's own coverage of TB2.1's "reward-hacking prevention" changes and the Terminal-Bench failure taxonomy's "Hallucination/guessing" and "Data fabrication or evaluator manipulation" categories: likely a score adjustment after discounting runs that gamed the verifier rather than genuinely solving the task. Confirm this interpretation with Will if it matters for the final report — don't state it as fact without checking.

## Grouped by underlying model (best score per model, any harness)

| Model | Provider | Best accuracy | Harness | Also seen with |
|---|---|---|---|---|
| Fable 5 | Anthropic | **83.8%** | Claude Code | Terminus 2 (80.4%) |
| GPT-5.5 | OpenAI | 83.1% | Codex | Terminus 2 (78.0%) |
| Grok 4.5 | xAI | 79.3%* | Cursor CLI | — |
| Opus 4.8 | Anthropic | 78.9% | Claude Code | — |
| GPT-5.6 Terra | OpenAI | 78.4% | Codex | — |
| Muse Spark 1.1 | Meta | 76.2% | mini-SWE-agent | — |
| GPT-5.6 Luna | OpenAI | 75.7% | Codex | — |
| Sonnet 5 | Anthropic | 74.6% | Claude Code | — |
| Gemini 3 Pro | Google | 73.9% | Terminus 2 | Gemini CLI (65.8%) |
| Opus 4.7 | Anthropic | 68.9% | Claude Code | Terminus 2 (66.1%) |
| Gemini 3.1 Pro | Google | 65.8% | Gemini CLI | Terminus 2 (65.6%) |
| GLM-5.1 | Zhipu | 58.7% | Claude Code | — |

*Grok 4.5's score carries the largest hack adjustment on the board (-9.0%) — treat as the least trustworthy top-5 result until that's understood.

## Key findings

1. **Fable 5 (Anthropic) is the strongest model on this benchmark, not Sonnet 5** — 83.8%/80.4% across two harnesses vs. Sonnet 5's 74.6%, and it's cheaper than GPT-5.5 for a comparable score ($552.67/$438.64 vs. $2,059.19). **This directly changes Q1's recommendation** — see below.
2. **Same harness, wildly different results purely from model choice:** Claude Code spans the entire board, from #1 (83.8%, Fable 5) to #17/last (58.7%, GLM-5.1). This is concrete evidence for *why* the brief requires holding the model constant — without that control, a harness comparison is meaningless.
3. **Grok 4.5's result is the most hack-adjusted on the board (-9.0%)** — worth flagging to Will as a reason to treat Cursor CLI/Grok 4.5 cautiously if it ever comes up as a baseline candidate.
4. OpenHands still doesn't appear on this snapshot (unchanged from the earlier check) — still a "not submitted," not "unsupported," situation per Harbor's own docs.

## Update this triggered

Q1 in [week-02-mentor-agenda-2026-08-05.md](week-02-mentor-agenda-2026-08-05.md) previously recommended Claude Sonnet 5 as the reference model. Updated to Fable 5 given the accuracy/cost evidence above — see that file for the current recommendation and reasoning.
