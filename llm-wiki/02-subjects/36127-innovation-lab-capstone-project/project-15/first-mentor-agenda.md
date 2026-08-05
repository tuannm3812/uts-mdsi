# Project 15 — First Mentor Meeting Agenda (Week 2)

* **Meeting Time:** Wednesday, 5 August 2026, 6:30 PM – 7:00 PM (30 minutes)
* **Location:** MS Teams
* **Attendees:**
  * **Team iLab 15-1:** Manh Tuan Nguyen (Team Leader), Daniel Alexander, Mukesh Murugesan, Manu Sasikanth Oruvilakode, Faisal Shoaib, Yash Raj Singh
  * **Mentor:** William Feng
* **Purpose:** Confirm the experimental contract, resource constraints, baseline harnesses, and feasibility parameters (milestone exit evidence for Week 2).

---

## Questions to Share with the Team (plain list)

Just the questions, no internal notes/recommendations — copy-paste this section for teammates.

1. Which exact model and reasoning effort settings must remain fixed for our custom-vs-baseline comparison?
2. Which two established harnesses should we pin for the baseline runs?
3. Will the university or the industry partner (Synogize) provide API keys/credits, or is there a specific MDSI/iLab compute environment allocated for our runs?
4. Is the 20-task development subset pre-selected by the client/mentor, or should the team select and freeze it ourselves?
5. How many repeated trials (runs) per task are expected during development and final evaluation?
6. What is the exact benchmark criterion for "beating" an established harness?
7. What infrastructure/Harbor runtime failures are we permitted to rerun, and how should we log and report these exceptions?
8. If our primary model configuration becomes cost-prohibitive, are we permitted to substitute a cheaper/faster model, as long as it remains constant across all harnesses?
9. What are the key deliverables expected by the client at the Week 5, Week 7, and Week 9 meetings?
10. What are the rules regarding public vs. private repository sharing, leaderboard submissions, and academic co-authorship for the final report?
11. What statistical standard counts as genuinely beating a harness — raw score, confidence interval, significance test, or directional improvement on the dev subset?
12. Is a public leaderboard submission a required deliverable, or best-effort?
13. Is there value or permission in coordinating with Team iLab 15-2 to share established-harness baseline runs?
14. Do you know whether the Proposal, Progress Report, Presentation, and Final Report are marked as group or individual submissions?

---

## Before the Agenda — Two Housekeeping Items

* **Roster check (Will asked for this explicitly):** His welcome message said he added members "based on the Allocations file" and to flag any discrepancy ASAP. Confirm at the top of the call that his roster matches: Manh Tuan Nguyen (leader), Daniel Alexander, Mukesh Murugesan, Manu Sasikanth Oruvilakode, Faisal Shoaib, Yash Raj Singh.
* **Group name — still not chosen as of this draft.** His action list asked for team leader + group name + timeslot together; leader and slot are settled, name is the one outstanding item. Pick one before the call.

---

## Master Question List — All Sources, Priority-Ranked

Consolidates the literature review's "Decisions requiring mentor or client confirmation," the subject kickoff requirements, and open items from `agent-collaboration-log.md`. Detailed context and our provisional recommendation for every item is in the numbered sections below (housekeeping items are above; questions 1–10 keep the same numbers as before, 11–14 are new).

**Tier 0 — Housekeeping, before the questions start**
- Confirm roster matches Will's Allocations file.
- State group name.

**Tier 1 — Critical, must ask live (blocks Week 3 tasks P15-013–018)**
1. Fixed model & reasoning settings
2. Two established harnesses
3. API/compute budget
4. Development-subset selection
5. Success definition ("beat")

**Tier 2 — Important, ask live if the first 5 don't eat the clock**
6. Repeated-trial expectations
7. Sandbox & rerun rules
11. *(new)* Statistical standard for claiming an improvement
12. *(new)* Is a leaderboard submission mandatory, or best-effort?
13. *(new)* Coordinate baseline runs with Team iLab 15-2?

**Tier 3 — Good to confirm, fine to follow up async on Teams after the call**
8. Model/provider fallback if primary is unaffordable
9. Client meeting deliverables (Week 5/7/9)
10. Repository, leaderboard, and attribution rules

**Tier 4 — Ask only if it comes up naturally; otherwise redirect to the subject coordinator**
14. *(new)* Group-vs-individual assessment ambiguity — this is Ali Anaissi's call, not Will's, per the kickoff slides' own conflicting wording.

---

## Required Agenda & Questions

### 1. Fixed Model & Reasoning Settings
* **Question:** Which exact model and reasoning effort settings must remain fixed for our custom-vs-baseline comparison?
* **Team Context:** The project brief requires holding the model constant to isolate harness-driven performance. We propose using a current-generation frontier model — **Claude Sonnet 5** (or **GPT-5.6 Terra**) — as the reference model, but need to confirm if there are reasoning-effort controls (e.g. reasoning effort level, temperature = 0 for reproducibility) we must freeze.
* **Provisional Recommendation:** Claude Sonnet 5 at a fixed, stated reasoning-effort level (e.g. "medium"), temperature `0.0` if the provider still exposes it.

### 2. Established Harness Baselines
* **Question:** Which two established harnesses should we pin for the baseline runs?
* **Team Context:** The official brief suggests **Claude Code** and **OpenHands** as examples. We also noticed Project 16 mentions **Codex CLI**. Pinning these early is critical for tasks P15-014 and P15-015 in Week 3.
* **Provisional Recommendation:** OpenHands and Claude Code (or Codex CLI if we coordinate with Team 15-2).

### 3. API Credits & Compute Budget
* **Question:** Will the university or the industry partner (Synogize/Dr. William So) provide API keys/credits, or is there a specific MDSI/iLab compute environment allocated for our runs?
* **Team Context:** Running 89 tasks on Terminal-Bench with high-tier models can easily cost $50–$150 per full run (plus repeated trials and development). We need a clear funding boundary to perform cost-scenarios in task P15-011.
* **Provisional Recommendation:** Ask for a confirmed funded ceiling (iLab-provided credits or Synogize sponsorship) first; if none exists, propose an initial self-funded cap for the 20-task dev subset only, and defer committing to full-89-task or leaderboard spend until Q12 is answered.

### 4. Development Subset Selection
* **Question:** Is the 20-task development subset pre-selected by the client/mentor, or should the team select and freeze it ourselves? If we select it, are there specific task category distributions (e.g., file manipulation, git operations, web search) we should target?
* **Team Context:** We need to freeze this subset by Week 3 (P15-016) to avoid selection bias (overfitting the custom harness to specific tasks).
* **Provisional Recommendation:** Team drafts a candidate 20-task subset stratified across TB2.1's task categories and brings it to Will for approval/adjustment, rather than waiting passively for one to be assigned.

### 5. Repeated Trial Expectations
* **Question:** How many repeated trials (runs) per task are expected during development and final evaluation to account for model variance?
* **Team Context:** Running each task 3–5 times provides a more robust statistical comparison but multiplies our API costs.
* **Provisional Recommendation:** 1 run per task during rapid prototyping on the 20-task dev subset, escalating to 3 runs for borderline/close comparisons and for the final 89-task evaluation — consistent with the paired-comparison standard proposed in Q11.

### 6. Success Definition ("Beat an Established Harness")
* **Question:** What is the exact benchmark criterion for "beating" an established harness? Does it require:
  1. A higher raw score on a single full run of all 89 tasks?
  2. A statistically significant higher average score over multiple full runs?
  3. Beating the baseline on the 20-task development subset?
  4. An accepted public submission to the `tbench.ai` leaderboard?
* **Team Context:** This directly gates when we can call the project "successful" for the final report and presentation — worth pinning down early rather than assuming.
* **Provisional Recommendation:** Propose option 3 (dev-subset win with directional confidence, per Q11) as the working development bar, confirmed by one full 89-task run at the end — without making leaderboard acceptance (option 4) a hard requirement for "success," since that adds an external dependency outside the team's control (see Q12).

### 7. Sandbox & Rerun Infrastructure Rules
* **Question:** What infrastructure/Harbor runtime failures are we permitted to rerun, and how should we log and report these exceptions?
* **Team Context:** Tasks might fail due to transient network issues, Docker container timeouts, or API rate limits rather than agent errors. We need clear rules on what constitutes a valid rerun versus a hard failure.
* **Provisional Recommendation:** Infrastructure/provider failures (timeouts, container crashes, rate limits) are rerun-eligible and logged in a separate failure category from genuine agent errors, capped at a fixed number of automatic reruns (e.g. 2) so failed trials can't be quietly resampled until they pass.

### 8. Alternative Model & Provider Fallbacks
* **Question:** If our primary model configuration becomes cost-prohibitive or runs into severe rate limits, are we permitted to substitute a cheaper/faster model (e.g., Claude Haiku 4.5 or GPT-5.6 Luna) as long as it remains constant across all harnesses?
* **Team Context:** Budget (Q3) is still unconfirmed, so there's a real chance the primary configuration becomes unaffordable partway through development — better to pre-agree a fallback now than negotiate a scope change mid-sprint.
* **Provisional Recommendation:** Pre-agree one specific fallback pair now (Claude Haiku 4.5 / GPT-5.6 Luna) so a mid-project swap doesn't require another mentor round-trip — with the explicit condition that once triggered, the fallback model is held constant across every harness for the remainder of the comparison.

### 9. Client Meeting Expectations
* **Question:** What are the key deliverables expected by the client (Dr. William So) at the Week 5 early progress, Week 7 midpoint, and Week 9 pre-final meetings?
* **Team Context:** We want to align our sprint deliverables with the client's expectations for demonstrations and evidence.
* **Provisional Recommendation:** Use the exit-evidence already defined for each milestone in `team-task-tracker.md` (e.g. Week 5 = evidence package + demo + baseline comparison) as the working assumption, and ask Will to confirm or adjust rather than starting from a blank page.

### 10. Repository, Leaderboard, & Academic Attribution
* **Question:** What are the rules regarding public vs. private repository sharing, leaderboard submissions on `tbench.ai`, and academic co-authorship for the final report?
* **Team Context:** We want to ensure we respect intellectual property rules while meeting the showcase and leaderboard outcomes.
* **Provisional Recommendation:** Default to a private repository through development, opening it (or specific artifacts) publicly only at final freeze/showcase with Will's and Synogize's sign-off; standard student authorship with mentor/client acknowledged, no client-proprietary material ever committed.

### 11. Statistical Standard for "Beat" *(new)*
* **Question:** What statistical standard counts as genuinely beating a harness — a raw score difference, a confidence interval, a significance test (e.g. McNemar's, since task outcomes are paired binary results), or is directional improvement on the frozen dev subset enough?
* **Team Context:** This is distinct from Q6 (which asks *what kind of run* counts) — this asks *how sure we need to be* the difference is real and not noise. It directly determines how many repeated trials (Q6) we actually need, so ideally gets answered in the same breath as Q6.
* **Provisional Recommendation:** Propose paired win/loss counts with a confidence interval on the dev subset as the working bar, formal significance testing reserved for the final 89-task claim if budget allows.

### 12. Is Leaderboard Submission Mandatory? *(new)*
* **Question:** Is a public `tbench.ai` leaderboard submission a required deliverable, or best-effort contingent on budget/access/publication approval?
* **Team Context:** The brief lists it under "Expected outcomes," but the literature review flags this as unconfirmed — official submission requires at least 5 trials per task (≥445 runs), which is a large budget commitment on top of development. Knowing whether it's mandatory changes how much of the budget (Q3) we reserve for it versus development iteration.
* **Provisional Recommendation:** Treat it as a best-effort stretch goal unless Will confirms it's mandatory, so the team doesn't over-commit budget toward the ≥445-run requirement before development is even frozen.

### 13. Coordinate Baseline Runs with Team iLab 15-2? *(new)*
* **Question:** Is there value or permission in coordinating with Team iLab 15-2 (the other Project 15 group under the same mentor) to share established-harness baseline runs, so both teams aren't paying twice for the same $50–150-per-run baselines?
* **Team Context:** Will's own welcome message tied Team 15-2 to a Codex CLI progress check-in, so he's already tracking both teams. If baselines can be shared (or at least cross-validated), that's real budget saved for both groups' custom-harness iteration. Only worth raising if Q3's budget answer suggests cost pressure.
* **Provisional Recommendation:** Raise it briefly as an open offer; if Will is receptive, follow up directly with Team 15-2's leader after the call rather than trying to resolve sharing logistics live on a 30-minute slot.

### 14. Group vs. Individual Assessment *(new, may not be Will's call)*
* **Question:** Do you know whether the Proposal, Progress Report, Presentation, and Final Report are marked as group or individual submissions? The kickoff slides state both (slides 8–11 say group, slide 12 says individual).
* **Team Context:** This is a subject-coordinator (Ali Anaissi) question, not really a project-mentor one — ask only if it comes up naturally or Will happens to know; otherwise raise it with Ali directly rather than spending call time on it.
* **Provisional Recommendation:** Don't spend call time waiting on this — if Will doesn't know offhand, action item is for Tuan to email/Canvas-message Ali Anaissi directly this week rather than leaving it unresolved into Week 5 (Proposal is due then).
