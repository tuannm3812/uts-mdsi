# Project 15 — Agent Collaboration Log

Shared, append-only log for open discussion between Tuan and whichever AI tools he's using on Project 15 (custom Terminal-Bench harness) — Claude, Codex, and Antigravity so far. Use it to hand off context between tools, think out loud, flag questions, and record findings that aren't yet formal decisions (formal team/mentor decisions still go in [meeting-and-decision-log.md](meeting-and-decision-log.md); experiment results still go in [experiment-register.md](experiment-register.md); task status still goes in [team-task-tracker.md](team-task-tracker.md)).

## How to use this log

- Append new entries at the bottom, in chronological order. Do not edit or delete past entries — correct forward instead.
- Every entry needs a date/time, an author tag, and a short context line.
- If an entry raises something unresolved, add it to **Open questions** below and remove it from there once it's answered (with a pointer to the entry that resolved it).
- Keep entries conversational — this is a scratchpad for thinking together, not a polished deliverable. Evidence and formal write-ups still belong in the other Project 15 files.
- Any participant (Tuan, or any AI tool he's using) can read, append to, or respond in this file. Sign your entry with your actual tool name so provenance stays clear as more tools join.

## Open questions

- What evidence exists for P15-001 through P15-006? (still not started/only in-progress as of 2 Aug)
- Is there a second Project 15 team ("Team iLab 15-2") also being mentored by William Feng, and if so, is any coordination/comparison expected between the two teams?

## Entries

### 2026-08-04 — Claude

**Context:** Tuan asked whether the full official Project 15 instructions were recorded anywhere. They weren't — the literature review's "Official Project 15 rationale" section was a paraphrase, and `drive-source-inventory.md` listed the source PDF (`01 Topic Lists/36127-capstone-project-list-spring-2026.pdf`, the 28 Jul revision that added Projects 15/16) as "extraction pending." The only PDF actually extracted before now (`36127-capstone-project-topics-spring-2026.pdf`, 26 Jul) predates that revision and doesn't contain Project 15 at all.

**Action taken:** Extracted the correct PDF with `pdftotext -layout`, saved the full 16-project raw text to [../sources/raw/36127-capstone-project-list-spring-2026.txt](../sources/raw/36127-capstone-project-list-spring-2026.txt), and pulled Project 15's entry into a clean verbatim capture at [official-brief-verbatim.md](official-brief-verbatim.md). Linked from this workspace README and updated `drive-source-inventory.md`.

**Verification:** The literature review's paraphrase checks out — the "16 percentage points" harness gap matches the brief's "up to 16 points apart" exactly. No drift found.

**New detail not previously captured anywhere:** the brief itself suggests **Claude Code and OpenHands** as example established harnesses (non-binding "e.g.") — relevant to P15-014/P15-015 (pin harness A/B) once the mentor confirms. Also pulled Project #16's brief while I was in the source (also Dr William So/Synogize, meta-harness router) — it names **Codex CLI** as a third example harness and states it's standalone from Project 15. Noted in case "Team iLab 15-2" from the mentor's welcome message turns out to be a Project 16 team rather than a second Project 15 team.

**Open questions / follow-ups:** None new — this just closes a source-capture gap. Existing open questions above are unaffected.
### 2026-08-02 — Claude

**Context:** Setting up this log at Tuan's request, so Claude Code and Codex can discuss Project 15 work openly with him in one place instead of siloed sessions.

**Notes:** Log created. Linked from [README.md](README.md) and the subject [README.md](../README.md). Current known state going in: Week 1 milestone (29 Jul) is past due with most Week 1 tasks (P15-001, 002, 006) still "Not started" and the three literature-review tasks (P15-003/004/005) marked "In progress" in [team-task-tracker.md](team-task-tracker.md). Week 2 mentor/feasibility confirmation is due 5 Aug 2026. Group-formation notes from 28 Jul list Project 14 as the top preference, but Tuan confirmed he's working on Project 15 — that earlier preference note is stale and can be disregarded.

**Open questions / follow-ups:** None yet — over to Tuan/Codex.

### 2026-08-02 — Codex

**Context:** Verified whether the existing Project 15 work and this new collaboration setup are visible on GitHub.

**Notes:** The established Capstone work is committed and pushed to `origin/main`. Commit `98ae087` contains the Vietnamese literature review; earlier Project 15 commits include the English review, detailed significance analysis, PDF layout improvements, team trackers, and workspace links. The main artifacts are under `research/` and `project-15/` in this subject folder.

The apparent progress mismatch comes from two separate facts:

- this collaboration log, the subject-level `AGENTS.md`, and their README links had not yet been committed when Claude created the first entry, so another clone or session could not discover them; and
- [team-task-tracker.md](team-task-tracker.md) records assigned team-member work. The existence of Codex-prepared literature and planning artifacts does not prove that Members 1–6 have completed their assigned readings, procedures, mentor preparation, or reviews, so those task statuses should not be marked done automatically.

**Handoff:** Pull the latest `main`, start with this log and [README.md](README.md), and use the existing literature and tracking artifacts as inputs. Update P15 task statuses only when the named owner/reviewer has supplied evidence.

**Open questions / follow-ups:** Confirm the six member names and actual Week 1 evidence before updating P15-001 through P15-006.

### 2026-08-02 — Claude

**Context:** Tuan reported the team is now formed, and shared the mentor's first contact message (MS Teams/Slack post).

**Notes:** First real mentor contact has happened. Mentor is **William Feng** (MDSI alumni 2023, ~7.5 yrs Telstra Data Insights Analyst, ~2.5 yrs iLab mentoring) — distinct from **William So** of Synogize, who authored the Project 15 project brief as industry provider/client. Do not conflate the two roles in the meeting log or elsewhere.

Mentor's action items, unresolved: nominate a team leader, pick a group name, and claim a Wednesday 6:30-8:30pm MS Teams slot. The message lists all four available half-hour slots as already claimed: Session 1 (6:30-7:00) = Team iLab 15-1, Session 2 (7:00-7:30) = Team iLab 06-1, Session 3 (7:30-8:00) = Team iLab 16-1, Session 4 (8:00-8:30) = Team iLab 15-2 — with a note attached to that last slot asking "do you have any review or feedback for codex progress." This implies a second Project 15 team (15-2) exists under the same mentor and has already been asked about their Codex CLI baseline progress — worth watching since Codex CLI is one candidate established harness for our own comparison.

Still waiting on Tuan for: which team (15-1/15-2/other), real member names, team leader nomination, group name preference, and realistic timeslot given the apparent clash.

**Open questions / follow-ups:** See Open questions above — need Tuan's answers before updating [meeting-and-decision-log.md](meeting-and-decision-log.md) and [team-task-tracker.md](team-task-tracker.md) with real names and the mentor-contact milestone.

### 2026-08-02 — Claude

**Context:** Tuan confirmed the team is **Team iLab 15-1** and supplied the six real names.

**Notes:** Replaced Member 1-6 placeholders with real names across [team-task-tracker.md](team-task-tracker.md), [experiment-register.md](experiment-register.md), [README.md](README.md), and the [literature review](../research/project-15-terminal-bench-literature-review.md), in positional order: 1=Daniel Alexander, 2=Mukesh Murugesan, 3=Manh Tuan Nguyen, 4=Manu Sasikanth Oruvilakode, 5=Faisal Shoaib, 6=Yash Raj Singh. This is a provisional mapping by existing task-tracker position, not by confirmed skills/preference — flagged as such in the tracker for rebalancing at the first team meeting. Also logged the mentor's Teams welcome message as a pre-meeting note in [meeting-and-decision-log.md](meeting-and-decision-log.md) under the Week 2 mentor-meeting section, and updated [README.md](README.md) Current Status with the mentor identity (William Feng, distinct from client contact William So) and outstanding action items.

**Open questions / follow-ups:** Team leader nomination, group name, and Wednesday timeslot are still unresolved — all four listed slots (15-1, 06-1, 16-1, 15-2) appear already claimed, so we may need to ask the mentor directly for another slot or confirm 15-1's slot is actually still 6:30-7:00pm. Codex/Tuan: flag if any of this mapping needs correcting once real skills/preferences are known.

### 2026-08-02 — Claude

**Context:** Tuan confirmed he is team leader and the team already secured the 6:30-7:00pm Wednesday slot (matches the Team iLab 15-1 claim already visible in the mentor's message, so no conflict).

**Notes:** Recorded as decision D-001 in [meeting-and-decision-log.md](meeting-and-decision-log.md) and reflected in [README.md](README.md) Current Status. Group name is the one remaining unresolved item from the mentor's action list.

**Open questions / follow-ups:** Group name — once picked, update README.md and the meeting log. Also still open: real Week 1 evidence for P15-001/002/006, and whether Team iLab 15-2 is a second Project 15 group worth coordinating with.

### 2026-08-05 — Antigravity

**Context:** Preparing for the first mentor meeting tonight at 6:30 PM (Wednesday catchup) and checking Codex/Claude progress on literature reviews and mentor questions.

**Notes:** Codex verified the git history and highlighted that although literature reviews are prepared in `research/`, task statuses P15-001 through P15-006 should remain in-progress or not started until team members provide actual evidence of completion. Claude verified the verbatim Project 15 brief and confirmed the teams, mentor (William Feng), and slot (6:30–7:00 PM Wednesday).

**Action taken:** Compiled the 10 core questions and background context from the literature review into a formal, standalone agenda document at [week-02-mentor-agenda-2026-08-05.md](week-02-mentor-agenda-2026-08-05.md) to address task P15-006. Marked task P15-006 as "In review" on the tracker.

**Open questions / follow-ups:** Group name is still pending. Tuan should use the drafted agenda for the meeting tonight and fill in the decisions and actions in [meeting-and-decision-log.md](meeting-and-decision-log.md) immediately afterward to satisfy the Week 2 milestone.

### 2026-08-05 — Claude

**Context:** Tuan stated he wants to work individually on Project 15 tasks rather than wait on teammates, then bring drafts to the team — reviewed Antigravity's new [week-02-mentor-agenda-2026-08-05.md](week-02-mentor-agenda-2026-08-05.md) given tonight's 6:30pm mentor meeting is imminent. (Note: a third tool, Antigravity, is now also editing this project — this log's intro line says "Tuan, Claude, and Codex," worth updating to include it.)

**Bug found and fixed — time-critical:** Question 1 and Question 8 recommended **Claude 3.5 Sonnet, GPT-4o, and GPT-4o-mini** as provisional model choices. All three are multiple generations stale as of Aug 2026 (current: Claude's 5-family — Opus 5/Sonnet 5/Haiku 4.5 — and OpenAI's GPT-5.6 Sol/Terra/Luna family, confirmed via web search). Recommending an obsolete model to the mentor tonight would have been an immediate credibility problem. Fixed both questions to reference Claude Sonnet 5 and GPT-5.6 Terra/Luna instead.

**Not otherwise re-reviewed in full** — only checked for factual/currency errors given the time pressure, not for completeness or structure. Tuan: worth a fast skim of the rest of the agenda before 6:30pm.

### 2026-08-05 — Claude

**Context:** Tuan confirmed he wants proactive help going forward (act on findings rather than waiting to be asked), asked me to keep working in this log, and asked for a prioritized mentor-question list ahead of tonight's meeting. Did the full completeness pass on [week-02-mentor-agenda-2026-08-05.md](week-02-mentor-agenda-2026-08-05.md) I'd deferred in the previous entry, cross-checked against the literature review's "Immediate mentor questions" (10 items, same list Antigravity operationalized — good, no drift) and the `meeting-and-decision-log.md` Week 2 "Required agenda" (also the same 10 items).

**Two gaps found and fixed:**
1. Will's welcome message explicitly asked groups to flag any roster discrepancy against his "Allocations file" ASAP — nothing in the agenda addressed this. Added a housekeeping section at the top of the agenda to confirm the roster live on the call.
2. **Group name is still unpicked** — it's one of the three things Will's action list asked for (leader/name/slot), and it's the only one not resolved. This blocks nothing in the tracker, but it's an explicit outstanding ask from the mentor and should be settled before or at the top of the call.

Minor fixes: added missing team-context line to Q6, fixed a stray-space typo in Q7.

**Assessment:** agenda is now meeting-ready. Full 10-question list + priority ranking (given the 30-min slot won't comfortably fit all 10 with introductions) given to Tuan directly in chat, not duplicated here.

**Open questions / follow-ups:** Group name (blocking, urgent — needed before tonight). Everything else from the Open Questions list above is unaffected by this entry.

### 2026-08-05 — Claude

**Context:** Tuan asked for a critical assessment of the existing 10 questions (add/remove anything?) plus a single consolidated, priority-ranked master list placed *before* the "Required Agenda & Questions" section in [week-02-mentor-agenda-2026-08-05.md](week-02-mentor-agenda-2026-08-05.md).

**Assessment:** none of the original 10 should be removed — all trace cleanly to either the literature review's 12-item "Decisions requiring mentor or client confirmation" list or the kickoff requirements, and match what's actually in [official-brief-verbatim.md](official-brief-verbatim.md). But cross-checking against that 12-item source list surfaced 2 it dropped, plus 2 more from this log's own history that never made it into any agenda draft:

- **Q11 (new) — statistical standard for "beat."** Lit review's item #12, silently folded into Q6 instead of asked separately. Distinct question: not *what kind of run counts* (Q6) but *how sure do we need to be the difference is real*, which determines how many repeated trials (Q7) are actually needed.
- **Q12 (new) — is leaderboard submission mandatory or best-effort?** Lit review's item #8. Matters because official submission needs ≥445 runs (5 trials × 89 tasks), a real budget commitment distinct from development iteration cost.
- **Q13 (new) — coordinate baseline runs with Team iLab 15-2.** Flagged in this log back on 2 Aug (Open Questions) but never operationalized into any agenda. Real potential budget saving given $50–150/run baselines, and Will already links the two teams (his welcome message tied 15-2 to a Codex CLI check-in).
- **Q14 (new, low priority) — group-vs-individual assessment ambiguity.** From kickoff-requirements' own conflicting slides. Flagged as probably not Will's call — redirect to Ali Anaissi unless he happens to know.

**Action taken:** Added a "Master Question List — All Sources, Priority-Ranked" section directly before "Required Agenda & Questions," tiered (0=housekeeping, 1=critical/live, 2=important/live-if-time, 3=async-followup-ok, 4=probably-wrong-person). Added full detail cards for Q11–14 matching the existing Q1–10 format (question / team context / recommendation).

**Open questions / follow-ups:** Same as previous entry — group name still the only blocking item.

### 2026-08-05 — Claude

**Context:** Tuan asked for a plain, share-with-teammates version of just the 14 questions (no internal context/recommendations), then asked to verify every one of the 14 actually has both a Team Context and a Provisional Recommendation filled in.

**Action taken:**
1. Added a "Questions to Share with the Team (plain list)" section right after the header, before all internal-notes sections — flat numbered list, question text only, explicitly labelled as copy-paste-safe for teammates.
2. Audited all 14 detail cards in "Required Agenda & Questions." **Missing recommendations found on Q3, Q4, Q5, Q6, Q7, Q9, Q10, Q12, Q13, Q14; Q8 was missing both fields entirely.** Filled in all of them with recommendations grounded in existing project artifacts (team-task-tracker.md milestones, the official brief, prior log entries) rather than generic filler — e.g. Q9 now points at the tracker's own milestone exit-evidence definitions instead of inventing new ones, Q6/Q11 were cross-referenced so the success-definition and statistical-standard recommendations agree with each other.
3. Verified completeness with a scripted check (grep count per question block) — all 14 now show exactly 2 matches for "Team Context" + "Provisional Recommendation."

**Open questions / follow-ups:** Group name still the only blocking item before tonight's call.

### 2026-08-05 — Claude

**Context:** Tuan has an internal team meeting before the mentor call and asked for discussion points to be added to [week-02-mentor-agenda-2026-08-05.md](week-02-mentor-agenda-2026-08-05.md).

**Action taken:** Added an "Internal Team Meeting — Before the Mentor Call" section right after the header, before the shareable question list. Seven points: decide the group name, roster check, team sanity-check on the provisional recommendations (they're proposals, not agreed team positions yet), assign who asks which question live, agree the ask order (Tier 1 first), a real status round-robin on P15-001–006 (ties to Tuan's individual-first workstyle), and picking a note-taker for the mentor call itself. Point 4 explicitly ties question-assignment to the Individual Contribution Factor's 20%-weighted participation criterion from the kickoff requirements, since right now these questions would otherwise all come from Tuan alone.

**Open questions / follow-ups:** Group name still blocking.

### 2026-08-05 — Claude

**Context:** Tuan asked to update all files needed to make this easier to manage, following the naming-convention discussion (week number vs. date for the recurring mentor-agenda files).

**Action taken:**
1. `git mv first-mentor-agenda.md` → `week-02-mentor-agenda-2026-08-05.md` (week-led, zero-padded, date kept for provenance — matches the week-based organization already used throughout `team-task-tracker.md` and `meeting-and-decision-log.md`).
2. Updated the live reference: `team-task-tracker.md` P15-006's deliverable link.
3. **Exception to the "don't edit past entries" rule, noted explicitly:** repaired the file-link target (not the surrounding text) in this log's 5 historical mentions of the old filename, since a pure rename cross-reference fix doesn't change what was said or decided — only silent rewrites of content/meaning are off-limits.
4. Discoverability gap fixed: `project-15/README.md` never actually linked the mentor-agenda file at all (checked — it wasn't there even under the old name). Added a "Weekly mentor-meeting agendas" section with the naming convention documented inline, so `week-03-...`, `week-04-...` etc. just get appended there going forward without re-deriving the pattern.
5. Updated both `README.md` and `AGENTS.md`'s stale "Tuan, Claude, and Codex" wording to reflect Antigravity now being a participant too (this log's own header already had that fix; the two other files hadn't caught up). Added the naming convention to `AGENTS.md`'s working conventions so any tool picking this up cold follows it automatically.

**Open questions / follow-ups:** Group name still the only blocking item before tonight's call.

### 2026-08-05 — Claude

**Context:** Tuan asked for insights from the live Terminal-Bench 2.1 leaderboard (tbench.ai/leaderboard/terminal-bench/2.1) ahead of the mentor call, to sanity-check the harness recommendation in [week-02-mentor-agenda-2026-08-05.md](week-02-mentor-agenda-2026-08-05.md).

**Finding — corrects an existing recommendation:** Fetched the live leaderboard (17 entries total, checked 5 Aug 2026). **OpenHands does not appear on it at all.** 7 harnesses do appear; most frequent are Claude Code (5 entries, top score 83.8%, Fable 5) and Terminus 2 — Harbor's own reference agent — (5 entries, 80.4% at $438.64, Fable 5). Codex appears 3 times, competitive at frontier settings (83.1%) but expensive ($2,059.19 at GPT-5.5, cheaper at GPT-5.6 Terra/Luna). Gemini CLI, Cursor CLI, and mini-SWE-agent appear once or twice each. Small/young leaderboard, so treat rank gaps cautiously — same caution Q11 already raises about statistical standards.

**Action taken:** Updated Q2's Team Context with the leaderboard data (source, date, entry count) and changed the Provisional Recommendation from "OpenHands and Claude Code" to **"Claude Code + Terminus 2"** — both have public evidence of working through Harbor, Terminus 2 is cheaper than Codex at comparable accuracy. Kept OpenHands/Codex CLI noted as fallbacks in case Will has a specific reason to prefer them.

**Caveat:** leaderboard data was fetched via WebFetch's page summarization, not read directly — numbers were cross-checked across two separate fetches and were consistent, but worth a manual glance at the live page if exact figures matter for the final report.

**Not yet done:** the Mukesh-questions harness-design Q&A from earlier today was offered as a support doc for P15-013 but not yet confirmed/created — still open if Tuan wants it.

**Open questions / follow-ups:** Group name still the only blocking item before tonight's call.

### 2026-08-05 — Claude

**Context:** Tuan resolved the group name directly (**"iLab Project 15"** — plain, not themed) and confirmed the Mukesh-questions Q&A should be saved as a support doc.

**Action taken:**
1. Group name propagated everywhere it was still pending: `README.md` Current Status, `meeting-and-decision-log.md`'s Week 2 pre-meeting note (and added as decision **D-002** in the Decision index), and both mentions in `week-02-mentor-agenda-2026-08-05.md` (housekeeping item struck through as resolved). Removed "What is the group name?" from this log's Open Questions — all three of Will's requested items (leader/name/slot) are now settled.
2. Created [harness-design-qa.md](harness-design-qa.md) — the 7 Mukesh questions mapped to the lit review's Experiments 1–5, task P15-034, and the existing experiment-register.md logging schema, explicitly framed as input for P15-013 (architecture doc, still unowned) rather than the deliverable itself. Linked from `README.md`.

**Open questions / follow-ups:** Real evidence for P15-001 through P15-006, and whether Team iLab 15-2 coordination is worth pursuing (also raised as Q13 in the mentor agenda). Nothing left blocking tonight's call.

### 2026-08-05 — Claude

**Context:** Tuan asked why the literature review and planning missed the live leaderboard, and whether the team needs more up-to-date information generally.

**Root cause (process note, not a one-off fix):** the literature review was built entirely from academic papers — stable, arXiv-verifiable, and correctly checked. The leaderboard is the opposite: live, mutable, changes weekly. It's cited as reference #10 in the lit review but was apparently never actually fetched — cited as "a place to look," not something read. Separately, Q2's original "OpenHands" recommendation was inherited directly from the brief's own example wording ("e.g. Claude Code, OpenHands") without independent verification. **Same root cause as the earlier Claude-3.5-Sonnet/GPT-4o bug in this same file:** stable knowledge (papers, brief text, architecture principles) doesn't go stale and was checked well; live/operational state (leaderboard rankings, current model lineup, pricing) does go stale and wasn't checked at all until explicitly asked.

**New finding, updates Q2 again:** checked Harbor's own docs (harborframework.com/docs/agents) — **OpenHands is pre-integrated/built into Harbor**, alongside Claude Code, Terminus-2, Copilot CLI, Codex CLI, Gemini CLI, Grok Build, Mini-SWE-Agent (and, coincidentally, Antigravity SDK). So OpenHands' absence from the leaderboard means "not yet submitted," not "unsupported" — setup cost is the same either way. Updated Q2's recommendation to keep Claude Code + Terminus 2 as the evidenced default, but explicitly frame OpenHands as a live option worth asking Will about (generating novel data vs. duplicating an evidenced comparison), rather than something ruled out by the earlier finding.

**Recommended going forward (not yet actioned, for discussion):** re-check live sources (leaderboard, Harbor's supported-agent list, current model/pricing) at each real decision point rather than only at document-writing time — specifically before the P15-014/015 baseline freeze (Week 3) and again before the Week 9 final-evaluation freeze, since this landscape can shift again by then.

**Open questions / follow-ups:** Same as previous entry. Added: should live-source re-checks become an explicit tracker/checklist item (e.g. in team-task-tracker.md's weekly close checklist) rather than only happening when someone asks?

### 2026-08-05 — Claude

**Context:** Tuan confirmed — turning the live-source-recheck habit from the previous entry into a standing, institutionalized rule rather than something that only happens on request.

**Action taken:**
1. `team-task-tracker.md` Milestones table: added explicit exit evidence to **Week 3** ("live leaderboard/Harbor-support recheck for the chosen baselines") and **Week 9** ("final live-source recheck — leaderboard, model lineup, pricing — before freeze") — the two points where a stale assumption would actually do damage (baseline pin, final claims).
2. `team-task-tracker.md` weekly close checklist: added a standing item — any leaderboard/harness-support/model/pricing claim used that week must be checked against a live source, with a pointer to today's log entries as the "why."
3. `AGENTS.md` working conventions: added the stable-vs-mutable-state distinction as an explicit rule, so any tool picking this project up cold inherits the habit rather than re-learning it from a fresh incident.

**Open questions / follow-ups:** Real evidence for P15-001 through P15-006, and Team iLab 15-2 coordination (Q13) — both unchanged from before.

### 2026-08-05 — Claude

**Context:** Tuan asked to look at the leaderboard again with a focus on models/engines (not just harnesses), and record the table properly. First real application of the live-source-recheck rule just institutionalized.

**Action taken:** Fetched full leaderboard detail (provider, date, effort level, and a previously-missed "Hacks" column) across two more targeted WebFetch calls, cross-checked against the earlier fetch — all consistent. Saved as [leaderboard-snapshot-2026-08-05.md](leaderboard-snapshot-2026-08-05.md), including a model-grouped view (best score per underlying model regardless of harness), not just the agent-grouped view from before. Linked from `README.md`'s new "Terminal-Bench leaderboard snapshots" section.

**Finding — corrects Q1, not just Q2 this time:** **Fable 5 (Anthropic) is the top-scoring model on the whole board (83.8%), not Sonnet 5 (74.6%)** — and cheaper than the next-best, GPT-5.5 ($552.67 vs. $2,059.19 for comparable accuracy). Updated Q1's provisional recommendation from Sonnet 5 to Fable 5. Concrete supporting evidence for *why* model choice matters as much as harness choice: Claude Code alone spans 58.7% to 83.8% depending purely on which model runs it.

**Also noted, not yet resolved:** a "Hacks" column (reward-hacking adjustment, e.g. Grok 4.5 at -9.0%) that wasn't caught on the first pass — the page gives no definition for it; interpretation in the snapshot file is inferred from the lit review's TB2.1 coverage, not confirmed. Worth asking Will if it becomes relevant to final-report claims.

**Open questions / follow-ups:** Same as before, plus: confirm what the leaderboard's "Hacks" column actually measures, if it matters later.

### 2026-08-05 — Claude

**Context:** Tuan asked how long a full Harbor/Terminal-Bench run takes and what it costs — input for P15-011 (cost model, not started).

**Findings:**
- **Cost:** real data, not estimate — leaderboard full-run costs range $134–$2,059 depending on model/effort; Fable 5 (our Q1 pick) runs ~$440–$550. **Unconfirmed:** whether that already reflects the ≥5-trials/task leaderboard submission requirement or just one trial — up to 5× budget difference depending on the answer.
- **Runtime: genuinely not published anywhere.** Checked tbench.ai run docs, Harbor's docs/GitHub README, and EvalScope's third-party integration — none state wall-clock duration. Confirmed only: `--n-concurrent` flag exists (examples show 4/8), per-task agent timeout is configurable with no universal default, build-phase timeout is a fixed 600s. Explicitly avoided using a 69–93 min/task figure found for a *different, harder* derivative benchmark (Long-Horizon-Terminal-Bench) since presenting it as a TB2.1 number would be misleading.

**Action taken:** Saved [cost-and-runtime-notes.md](cost-and-runtime-notes.md) as P15-011 input, linked from README.md. Updated Q3's context in the mentor agenda with the real cost range and the trial-count uncertainty, and pointed at P15-009 (oracle smoke test, not started) as the team's actual mechanism for getting a real runtime number rather than guessing.

**Open questions / follow-ups:** Same as before, plus whether leaderboard costs include multiple trials — both good candidates to fold into tonight's Q3/Q11 discussion if time allows.

### 2026-08-05 — Claude

**Context:** The mentor meeting happened. Team formally confirmed Tuan as leader; William Feng couldn't answer the technical questions (his role doesn't cover project-specific content) and deferred all of Tier 1/2 to next week with William So (Synogize, the actual project provider). Tuan also proposed this week's individual-report task: everyone reads a paper and writes their own questions.

**Real bug found while checking this against the plan:** `team-task-tracker.md`'s P15-003/004/005/006 reading assignments **did not match** the literature review's own "Six-member reading allocation" table — both got the same positional Member-N→name substitution on 2 Aug, but the underlying Member numbering in the two documents was never the same scheme to begin with. Concretely: task tracker had Manh Tuan Nguyen on Terminal-Bench (P15-003), but the lit review's allocation had always intended Daniel Alexander for that paper; similarly Mukesh Murugesan's SWE-agent reading was mis-assigned to Manu Sasikanth Oruvilakode; and P15-005 bundled three papers (OpenHands, Agentless, OpenHands SDK) under Faisal alone when the lit review deliberately splits them three ways with cross-pair-boundary reviewers. Nothing had been produced yet under the wrong assignment, so zero cost to fix now — corrected P15-003/004/005/006's primary/reviewer fields and the ownership-balance table to match the lit review's original (well-designed, cross-pair-reviewed) mapping. The lit review's mapping was treated as canonical since it's the source design, not a later derivative.

**Tracker updated for the meeting outcome:** P15-010 (mentor discussion) marked **Blocked**, not "Not started" — the meeting happened but the technical contract wasn't confirmed. P15-011/012 (dependent) also marked Blocked. `meeting-and-decision-log.md`'s Week 2 Notes/Decisions/Actions filled in with what actually happened (was fully blank template before) — flagged a real schedule risk: Week 3's deliverables (P15-013–018) all depend on P15-010, and if William So's answers only land "next week," Week 3 has very little runway once the contract lands. Recommended pre-drafting P15-013–018 under the mentor agenda's provisional recommendations so the team can move fast once unblocked.

**Not yet recorded:** the specific admin protocol William Feng gave — Tuan to supply details so it can be logged accurately rather than assumed.

**Assessment of the reading-week plan (given directly to Tuan in chat, summary here):** good core idea, sharpened by (1) using the now-fixed six-member allocation with its already-defined output spec (one-pager, 3 findings, 2 limitations, 2 implications, 1 candidate experiment, 1 mentor question, citations) instead of an unscoped "read papers," (2) routing each person's generated mentor-question into pressure-testing the master question list before the William So session — turns it into real prep, not a disconnected exercise, and diversifies the question list beyond AI-authored input, (3) requiring each person's output committed as an evidenced artifact to finally close P15-003/004/005/006's evidence gap.

**Open questions / follow-ups:** Admin protocol details (from Tuan). Real per-person evidence for the now-corrected P15-003/004/005/006. Everything else unchanged.

### 2026-08-05 — Claude

**Context:** Tuan supplied the admin-protocol detail, reported teammates are asking what to put in their Week 2 individual report, and asked whether to create the team GitHub repo now.

**Action taken:**
1. Recorded the admin protocol in `meeting-and-decision-log.md`: William Feng clarified he's the liaison between the team and Synogize (not a technical source himself), gave a check-in meeting calendar/cadence, full details pending a slide Tuan will share.
2. Created [week-02-individual-report-guidance.md](week-02-individual-report-guidance.md) — the real, honest factual basis for everyone's Week 2 report: what's actually done (team/leader/mentor-contact), what's honestly blocked (P15-010), the corrected per-person reading table, what evidence exists vs. what's still missing (nobody has an individual reading artifact yet — that's 65% of the contribution score, so it's this week's real task). Linked from README.md.

**Repo question — answered, not yet executed:** recommended yes, create it now — P15-001 (Slack/GitHub governance, owned by Daniel, overdue since 29 Jul) and P15-007/008/009 (Docker/Harbor setup, oracle smoke test) don't depend on William So's answers, so there's no reason to keep waiting on infrastructure. `gh` is authenticated as `tuannm3812` with repo/admin:org scopes, so I can create it directly — but held off actually running it since repo name, visibility, and org/personal-account choice are Tuan's call and creating + inviting the mentor/team is a visible, not-cheaply-reversible action. Recommended private (matches the design decision already in the mentor agenda's Q10), and adding all 6 members + William Feng as collaborators per the kickoff requirement to add the mentor to the Git project.

**Open questions / follow-ups:** Repo name/visibility/org confirmation from Tuan before creating. Full admin-protocol slide once shared. Real per-person reading evidence, still open.

### 2026-08-05 — Claude

**Context:** Tuan confirmed repo name/visibility and asked me to create it, clone it locally, and set up governance — he'll add teammates/mentor as collaborators himself once he's collected GitHub usernames, so I did not add anyone.

**Action taken:**
1. Created `tuannm3812/ilab-project-15-terminal-bench-harness` (private) via `gh repo create`, cloned to `~/Documents/GitHub/1. Study/ilab-project-15-terminal-bench-harness` (matches the existing sibling-repo convention for Tuan's other coursework).
2. Added `README.md` (project summary, status disclaimer that the experimental contract isn't confirmed yet, team list, no setup instructions yet since infra isn't started), `CONTRIBUTING.md` (git workflow: task-ID branches, PR + 1 reviewer required, never commit secrets/client-confidential material, explicitly no LICENSE file yet since public/redistribution terms aren't confirmed), `.gitignore` (Python/Docker/secrets/OS junk). Committed and pushed to `main`.
3. Created 11 project-specific issue labels (type: governance/infrastructure/research/architecture/experiment/evaluation/client-facing, priority: critical/high/medium/low, plus blocked/needs-review) — kept GitHub's own defaults (bug, enhancement, question, etc.) rather than deleting them.
4. **Branch protection blocked:** `gh api` returned 403 — GitHub's free tier doesn't support branch protection on private repos, Pro is required. Recommended the GitHub Student Developer Pack (free Pro for students) as the fix. Documented the "PR + 1 review, no direct push" rule in CONTRIBUTING.md as a team convention in the meantime, not yet technically enforced.
5. Marked P15-001 "In review" (not Done — needs Daniel/Faisal's actual review per the tracker's own evidence standard) with the repo link and the branch-protection caveat. Linked the repo from `README.md` Current Status.

**Open questions / follow-ups:** Branch protection once Pro is available. Collaborators (Tuan adding directly). Slack setup still outstanding for full P15-001 closure. Everything else unchanged.

