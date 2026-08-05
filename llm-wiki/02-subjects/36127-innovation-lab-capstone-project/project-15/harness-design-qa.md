# Harness Design Q&A — Input for P15-013

Answers to Mukesh Murugesan's harness-design questions (5 Aug 2026), mapped against what the [literature review](../research/project-15-terminal-bench-literature-review.md) already researched and planned. **This is input material for P15-013 (architecture document, currently unowned/not started), not the architecture document itself** — whoever picks up P15-013 should start from here rather than re-deriving these answers from scratch.

Headline finding: every one of Mukesh's questions independently arrived at something the lit review already defined as one of the five planned ablations (Experiments 1–5) or an already-scoped tracker task. That's a good cross-check that the plan holds up against real engineering questions.

---

## 1. Trimming long command output (e.g. `pip install`, `git log`)

**Maps to:** Experiment 4 ("Context management") and the recommended architecture's "Bounded observation processor" component.

**Recommendation:** Never send raw hundred-line output to the model. Truncate to head+tail with an explicit "N lines omitted" marker — never silently drop error-relevant content (SWE-agent's principle: feedback should be "informative but concise"). Don't hand-pick one truncation strategy and lock it in — full-history vs. sliding-window vs. state-summary is literally one of the team's planned ablations, so implement it as a configurable setting from day one, not a hardcoded default.

## 2. Full raw bash vs. limited helper tools (`read_file` / `write_file` / `run_command`)

**Maps to:** Experiment 5 ("Tool granularity") — this is SWE-agent's core research question.

**Recommendation:** For the *first working version*, use one general terminal interface. The brief itself requires "the minimum harness that runs the tasks, not a general framework," and the recommended architecture's "Tool interface" component is scoped to "parse and validate requested terminal actions," not a large tool library. Structured-vs-general isn't a day-one lock-in decision — it's what Experiment 5 is designed to measure later.

## 3. Raw error shown to the model, or forced pause-and-explain before retry?

**Maps to:** Experiment 3 ("Error-aware repair").

**Recommendation:** Both, not either/or. Show the raw error (don't summarize away signal), but require an explicit diagnosis step before the retry action is accepted. This directly targets Terminal-Bench's own "Repetition" failure category (ineffective action repeated without new evidence) and "Reasoning-action mismatch" category.

## 4. Detecting and cutting off repeated identical failing commands

**Maps to:** task **P15-034** ("Add repetition, parser-error, and budget-exhaustion safeguards," Week 8, not yet started).

**Recommendation:** Hash/normalize the last N actions; if the same command+error repeats (e.g. 2×), hard-interrupt and force a new diagnosis before continuing (same mechanism as Q3), logged under the "Repetition" failure category rather than silently retrying forever.

## 5. Sliding window vs. summarize near the token limit

**Maps to:** Experiment 4 again, with a stated working hypothesis: **H4 — "state summary plus recent evidence will use fewer tokens than full history with no loss of accuracy."**

**Recommendation:** Implement the state-summary approach as the default/recommended treatment, but keep sliding-window as the comparison condition — this is meant to be measured empirically, not assumed correct.

## 6. Prompt style for the 20-task testing phase (step-by-step vs. structured JSON)

**Maps to:** Experiment 1 ("Prompt structure"), hypothesis **H1**.

**Recommendation:** Use the explicit staged **inspect → plan → execute → verify → repair-once** workflow as the baseline prompt structure for the whole dev-subset phase, versus a plain direct-completion prompt as the control condition.

## 7. What else to log besides accuracy/tokens/cost

**Already fully specified — no new design needed.** `experiment-register.md`'s trial-level table already has: reward, input/output tokens, cost, runtime, retries, error, failure category, trajectory path. The lit review's "Secondary outcomes" list adds: number of model turns, number of terminal actions, timeout rate, infrastructure error rate, verification coverage, repeated-action rate.

**Recommendation:** Implement logging to match that existing schema directly — don't design a new one.

---

## Summary table

| # | Question | Maps to | One-line recommendation |
|---|---|---|---|
| 1 | Trimming long output | Experiment 4, "Bounded observation processor" | Truncate head+tail with omission marker; make strategy configurable |
| 2 | Raw bash vs. helper tools | Experiment 5 | Start general (minimum harness); structured-vs-general is a later ablation |
| 3 | Raw error vs. forced explain | Experiment 3 | Both — show raw error, require diagnosis before retry |
| 4 | Repeated failing commands | P15-034 | Hash/compare last N actions, hard-interrupt on repeat, log as "Repetition" |
| 5 | Sliding window vs. summarize | Experiment 4, H4 | Default to state summary, keep sliding-window as comparison condition |
| 6 | Prompt style for dev-subset phase | Experiment 1, H1 | Staged inspect→plan→execute→verify→repair-once as baseline |
| 7 | What else to log | `experiment-register.md` schema | Already specified — implement against existing columns |
