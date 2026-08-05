# Project 15 — First Mentor Meeting Agenda (Week 2)

* **Meeting Time:** Wednesday, 5 August 2026, 6:30 PM – 7:00 PM (30 minutes)
* **Location:** MS Teams
* **Attendees:**
  * **Team iLab 15-1:** Manh Tuan Nguyen (Team Leader), Daniel Alexander, Mukesh Murugesan, Manu Sasikanth Oruvilakode, Faisal Shoaib, Yash Raj Singh
  * **Mentor:** William Feng
* **Purpose:** Confirm the experimental contract, resource constraints, baseline harnesses, and feasibility parameters (milestone exit evidence for Week 2).

---

## Before the Agenda — Two Housekeeping Items

* **Roster check (Will asked for this explicitly):** His welcome message said he added members "based on the Allocations file" and to flag any discrepancy ASAP. Confirm at the top of the call that his roster matches: Manh Tuan Nguyen (leader), Daniel Alexander, Mukesh Murugesan, Manu Sasikanth Oruvilakode, Faisal Shoaib, Yash Raj Singh.
* **Group name — still not chosen as of this draft.** His action list asked for team leader + group name + timeslot together; leader and slot are settled, name is the one outstanding item. Pick one before the call.

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

### 4. Development Subset Selection
* **Question:** Is the 20-task development subset pre-selected by the client/mentor, or should the team select and freeze it ourselves? If we select it, are there specific task category distributions (e.g., file manipulation, git operations, web search) we should target?
* **Team Context:** We need to freeze this subset by Week 3 (P15-016) to avoid selection bias (overfitting the custom harness to specific tasks).

### 5. Repeated Trial Expectations
* **Question:** How many repeated trials (runs) per task are expected during development and final evaluation to account for model variance?
* **Team Context:** Running each task 3–5 times provides a more robust statistical comparison but multiplies our API costs. We recommend 1 run during rapid prototyping on the 20-task subset, and 3 runs for final evaluation on the 89 tasks.

### 6. Success Definition ("Beat an Established Harness")
* **Question:** What is the exact benchmark criterion for "beating" an established harness? Does it require:
  1. A higher raw score on a single full run of all 89 tasks?
  2. A statistically significant higher average score over multiple full runs?
  3. Beating the baseline on the 20-task development subset?
  4. An accepted public submission to the `tbench.ai` leaderboard?
* **Team Context:** This directly gates when we can call the project "successful" for the final report and presentation — worth pinning down early rather than assuming.

### 7. Sandbox & Rerun Infrastructure Rules
* **Question:** What infrastructure/Harbor runtime failures are we permitted to rerun, and how should we log and report these exceptions?
* **Team Context:** Tasks might fail due to transient network issues, Docker container timeouts, or API rate limits rather than agent errors. We need clear rules on what constitutes a valid rerun versus a hard failure.

### 8. Alternative Model & Provider Fallbacks
* **Question:** If our primary model configuration becomes cost-prohibitive or runs into severe rate limits, are we permitted to substitute a cheaper/faster model (e.g., Claude Haiku 4.5 or GPT-5.6 Luna) as long as it remains constant across all harnesses?

### 9. Client Meeting Expectations
* **Question:** What are the key deliverables expected by the client (Dr. William So) at the Week 5 early progress, Week 7 midpoint, and Week 9 pre-final meetings?
* **Team Context:** We want to align our sprint deliverables with the client's expectations for demonstrations and evidence.

### 10. Repository, Leaderboard, & Academic Attribution
* **Question:** What are the rules regarding public vs. private repository sharing, leaderboard submissions on `tbench.ai`, and academic co-authorship for the final report?
* **Team Context:** We want to ensure we respect intellectual property rules while meeting the showcase and leaderboard outcomes.
