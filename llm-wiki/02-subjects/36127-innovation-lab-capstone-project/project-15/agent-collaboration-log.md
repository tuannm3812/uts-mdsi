# Project 15 — Agent Collaboration Log

Shared, append-only log for open discussion between Tuan, Claude, and Codex while working on Project 15 (custom Terminal-Bench harness). Use it to hand off context between tools, think out loud, flag questions, and record findings that aren't yet formal decisions (formal team/mentor decisions still go in [meeting-and-decision-log.md](meeting-and-decision-log.md); experiment results still go in [experiment-register.md](experiment-register.md); task status still goes in [team-task-tracker.md](team-task-tracker.md)).

## How to use this log

- Append new entries at the bottom, in chronological order. Do not edit or delete past entries — correct forward instead.
- Every entry needs a date/time, an author tag, and a short context line.
- If an entry raises something unresolved, add it to **Open questions** below and remove it from there once it's answered (with a pointer to the entry that resolved it).
- Keep entries conversational — this is a scratchpad for thinking together, not a polished deliverable. Evidence and formal write-ups still belong in the other Project 15 files.
- Any of the three participants (Tuan, Claude, Codex) can read, append to, or respond in this file.

## Open questions

- What evidence exists for P15-001 through P15-006? (still not started/only in-progress as of 2 Aug)
- What is the group name? (leader and timeslot are now resolved — see 2 Aug decision below)
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

**Action taken:** Compiled the 10 core questions and background context from the literature review into a formal, standalone agenda document at [first-mentor-agenda.md](first-mentor-agenda.md) to address task P15-006. Marked task P15-006 as "In review" on the tracker.

**Open questions / follow-ups:** Group name is still pending. Tuan should use the drafted agenda for the meeting tonight and fill in the decisions and actions in [meeting-and-decision-log.md](meeting-and-decision-log.md) immediately afterward to satisfy the Week 2 milestone.

