# Project 15 Meeting and Decision Log

## How to use this log

- Create one section per formal team, mentor, or client meeting.
- Record decisions with rationale, not only discussion.
- Give every action one owner, one reviewer where relevant, and one due date.
- Link Slack notes, GitHub issues, documents, code, or experiment artifacts.
- Carry unresolved questions into the next relevant agenda.

## Decision index

| Decision ID | Date | Decision | Rationale | Owner | Evidence |
|---|---|---|---|---|---|
| D-001 | 2 Aug 2026 | Team leader is Manh Tuan Nguyen; MS Teams slot is Wednesday 6:30-7:00pm | Mentor requested both by reply; slot matches the already-listed Team iLab 15-1 claim | Manh Tuan Nguyen | Reported by Tuan in agent-collaboration-log.md |
| D-002 | 5 Aug 2026 | Group name is "iLab Project 15" | Mentor requested a group name alongside leader/slot; team went with the plain/direct option rather than a themed name | Manh Tuan Nguyen | Reported by Tuan in agent-collaboration-log.md |

---

## First mentor meeting - Week 2

**Target date:** 5 Aug 2026
**Purpose:** Confirm experimental contract, resources, scope, and communication process.

### Pre-meeting contact — 2 Aug 2026 (Teams post, not yet the 30-min meeting)

Mentor **William Feng** posted a welcome message in the group's MS Teams channel. He is MDSI alumni (2023), ~7.5 yrs telco/Telstra Data Insights Analyst experience, ~2.5 yrs mentoring iLab. Weekly catchups will run 30 minutes on Wednesdays between 6:30-8:30pm; exact slot is first-come-first-served. He asked each group to reply nominating a team leader, a group name, and a timeslot. As of this post, the four available half-hour slots were already claimed by other teams (Team iLab 15-1, 06-1, 16-1, and 15-2 — note Team iLab 15-2 appears to be a second group also working Project 15, and was asked separately about Codex CLI baseline progress). Team leader, group name, and slot: team leader is **Manh Tuan Nguyen** (resolved 2 Aug 2026), timeslot is Wednesday **6:30-7:00pm** (matches the already-listed Team iLab 15-1 slot, so no conflict). Group name is **iLab Project 15** (resolved 5 Aug 2026) — all three of the mentor's requested items are now settled.

### Required agenda

1. Confirm Terminal-Bench 2.1 dataset and 89-task scope.
2. Confirm the fixed model and reasoning settings.
3. Select two established harnesses.
4. Confirm API credits, compute, and sandbox resources.
5. Confirm how the 20-task development subset will be selected.
6. Confirm repeated-trial expectations.
7. Define “beat an established harness.”
8. Confirm infrastructure rerun and exclusion rules.
9. Confirm Week 5 client deliverable.
10. Confirm repository and leaderboard attribution.

### Notes

- **Meeting happened 5 Aug 2026.** William Feng could not answer the technical/experimental-contract questions (Required agenda items 1–10 above, and the fuller list in [week-02-mentor-agenda-2026-08-05.md](week-02-mentor-agenda-2026-08-05.md)) — those need Dr William So (Synogize, the project's industry provider), not the iLab mentor. He clarified his own role: he's the **middle-person between the team and industry personnel**, not a source of technical answers himself. Admin protocol he gave: a **check-in meeting calendar/cadence** (details on a slide Tuan will share and add here later) and how he can help procedurally. Said to wait until next week for William So on the technical questions.
- **Schedule risk worth flagging:** Week 3 (12 Aug) milestone deliverables — architecture, baseline protocol, frozen dev subset (P15-013 to P15-018) — all depend on P15-010's outputs (model, harnesses, budget, dev-subset, success definition). If William So's answers only land "next week," Week 3 has very little runway to actually execute once the contract is confirmed. Worth pre-drafting P15-013–018 under the provisional recommendations already in the mentor agenda so the team can move fast the moment answers arrive, rather than starting from zero.

### Decisions

| Decision ID | Decision | Rationale | Approved by | Evidence |
|---|---|---|---|---|
| D-003 | Team leader nomination formally confirmed by the team (not just self-declared) | Discussed and agreed at the 5 Aug meeting | Team, led by William Feng's request | Reported by Tuan in agent-collaboration-log.md |

### Actions

| Action | Owner | Reviewer | Due | Status | Evidence |
|---|---|---|---|---|---|
| Follow admin protocol from William Feng (check-in calendar/cadence) | Whole team | Manh Tuan Nguyen | TBD | In progress | Full slide pending from Tuan — update this row once shared |
| Bring full technical question list to William So | Manh Tuan Nguyen | — | Next mentor session | Not started | [week-02-mentor-agenda-2026-08-05.md](week-02-mentor-agenda-2026-08-05.md) |

### Unresolved questions

-

---

## Early progress client meeting - Week 5

**Target date:** 26 Aug 2026
**Purpose:** Demonstrate reproducible infrastructure, baseline protocol, and initial evidence.

### Proposed evidence package

- frozen problem statement and research questions;
- system architecture;
- successful Harbor/oracle smoke tests;
- selected model and baselines;
- frozen 20-task development subset;
- cost estimate and risk register;
- initial baseline results;
- custom harness skeleton; and
- next-stage experiment plan.

### Notes

-

### Decisions and feedback

| Decision ID | Decision/feedback | Rationale or implication | Owner | Evidence |
|---|---|---|---|---|
|  |  |  |  |  |

### Actions

| Action | Owner | Reviewer | Due | Status | Evidence |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

---

## Midpoint client review - Week 7

**Target date:** 9 Sep 2026
**Purpose:** Demonstrate custom harness V1 and controlled comparisons.

### Proposed evidence package

- established baselines;
- custom minimal baseline;
- first prompt and verification ablations;
- cost, token, and runtime results;
- trajectory examples;
- failure taxonomy;
- validity limitations; and
- refined Week 8 experiment priorities.

### Notes

-

### Decisions and feedback

| Decision ID | Decision/feedback | Rationale or implication | Owner | Evidence |
|---|---|---|---|---|
|  |  |  |  |  |

### Actions

| Action | Owner | Reviewer | Due | Status | Evidence |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

---

## Pre-final client meeting - Week 9

**Target date:** 30 Sep 2026
**Purpose:** Freeze the harness and final evaluation protocol.

### Required decisions

- final harness configuration;
- final model and infrastructure confirmation;
- full-run trial count;
- rerun and exclusion policy;
- budget approval;
- statistical analysis;
- leaderboard submission feasibility; and
- presentation narrative.

### Notes

-

### Design-freeze record

| Item | Frozen value or link | Approved by | Evidence |
|---|---|---|---|
| Git commit/tag |  |  |  |
| Dataset |  |  |  |
| Model and reasoning effort |  |  |  |
| Harness configuration |  |  |  |
| Prompt |  |  |  |
| Tools |  |  |  |
| Context |  |  |  |
| Verification/retry |  |  |  |
| Trial and rerun policy |  |  |  |

### Actions

| Action | Owner | Reviewer | Due | Status | Evidence |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

---

## Final presentation review - Week 11

**Target date:** 14 Oct 2026
**Purpose:** Confirm the final evidence, claims, limitations, and presentation delivery.

### Review checklist

- [ ] Every claim is supported by a result or source
- [ ] Harness/model comparisons are fair
- [ ] Costs and failed trials are disclosed
- [ ] Limitations and threats to validity are explicit
- [ ] Demonstration is reproducible
- [ ] Each member has a speaking role
- [ ] Q&A owners are assigned
- [ ] Backup demonstration material exists

### Notes, decisions, and actions

| Item | Owner | Reviewer | Due | Status | Evidence |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

---

## Showcase and handover retrospective - Week 12

**Target date:** 21 Oct 2026
**Purpose:** Deliver final artifacts and capture lessons for the client, team, and future work.

### Handover checklist

- [ ] Reproducible repository and setup instructions
- [ ] Frozen final configuration
- [ ] Raw and processed result locations
- [ ] Experiment register complete
- [ ] Known limitations and unresolved defects
- [ ] Cost and infrastructure notes
- [ ] Final report and presentation
- [ ] Client-approved public/private artifact boundaries
- [ ] Leaderboard submission status
- [ ] Maintenance or future-research recommendations

### Retrospective

**What worked:**

-

**What did not work:**

-

**What we would change:**

-

**Future research:**

-
