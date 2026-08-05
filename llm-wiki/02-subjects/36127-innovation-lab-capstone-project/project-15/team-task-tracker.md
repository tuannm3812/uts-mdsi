# Project 15 Team Task Tracker

## Milestones

| Period | Date | Milestone | Exit evidence |
|---|---:|---|---|
| Week 1 | 29 Jul 2026 | Team and research setup | Team procedures, literature allocation, skills survey, mentor questions |
| Week 2 | 5 Aug 2026 | Mentor and feasibility confirmation | Confirmed experimental contract, smoke test, cost/compute decision |
| Week 3 | 12 Aug 2026 | Experimental design | Architecture, baseline protocol, frozen development subset |
| Week 4 | 19 Aug 2026 | Baseline readiness | Reproducible established harness runs and custom skeleton |
| Week 5 | 26 Aug 2026 | Early progress client meeting | Evidence package, demonstration, feedback and revised actions |
| Week 6 | 2 Sep 2026 | Custom harness V1 | Minimal harness plus first controlled experiments |
| Week 7 | 9 Sep 2026 | Midpoint client review | Baseline comparison, V1 results, failure analysis |
| Week 8 | 16 Sep 2026 | Harness refinement | Context, recovery, verification, or tool ablations |
| STUVAC | 23 Sep 2026 | Consolidation and contingency | Reproduced key results, draft methods/results, resolved technical debt |
| Week 9 | 30 Sep 2026 | Pre-final client meeting | Final design and evaluation protocol frozen |
| Week 10 | 7 Oct 2026 | Final evaluation and analysis | Full results, statistics, report-ready figures and limitations |
| Week 11 | 14 Oct 2026 | Final presentation | Rehearsed presentation, Q&A, backup demonstration |
| Week 12 | 21 Oct 2026 | iLab Showcase and handover | Reproducible repository, final artifacts, retrospective |

## Ownership rules

- Every task has one primary owner and one reviewer.
- A reviewer must inspect evidence before a task becomes `Done`.
- Primary ownership is initially balanced at eight tasks per member.
- Reviews cross pair boundaries wherever possible.
- Real names confirmed 2 Aug 2026: Daniel Alexander, Mukesh Murugesan, Manh Tuan Nguyen, Manu Sasikanth Oruvilakode, Faisal Shoaib, Yash Raj Singh — mapped below in that order, provisionally, by task-tracker position, not yet by skills or preference; rebalance at the first team meeting.
- Split a task when it becomes too large to verify within one weekly cycle.

## Task register

| ID | Week | Due | Workstream | Task | Primary | Reviewer | Priority | Status | Dependency | Deliverable/evidence |
|---|---|---:|---|---|---|---|---|---|---|---|
| P15-001 | 1 | 29 Jul | Governance | Create Slack structure, GitHub repository rules, issue labels, and review procedure | Daniel Alexander | Faisal Shoaib | High | Not started | None | Workspace links and procedure |
| P15-002 | 1 | 29 Jul | Governance | Run six-member skills, availability, hardware, and learning-goal survey | Mukesh Murugesan | Yash Raj Singh | High | Not started | None | Completed skills matrix |
| P15-003 | 1 | 30 Jul | Research | Summarise Terminal-Bench benchmark contract and failure taxonomy | Manh Tuan Nguyen | Daniel Alexander | High | In progress | Literature review | One-page evidence note |
| P15-004 | 1 | 30 Jul | Research | Summarise SWE-agent ACI design and ablations | Manu Sasikanth Oruvilakode | Mukesh Murugesan | High | In progress | Literature review | One-page evidence note |
| P15-005 | 1 | 31 Jul | Research | Summarise OpenHands, Agentless, and OpenHands SDK implications | Faisal Shoaib | Manh Tuan Nguyen | High | In progress | Literature review | Comparison notes |
| P15-006 | 1 | 31 Jul | Planning | Consolidate mentor questions, risks, terminology, and project assumptions | Yash Raj Singh | Manu Sasikanth Oruvilakode | High | In review | P15-003 to P15-005 | [first-mentor-agenda.md](first-mentor-agenda.md) |
| P15-007 | 2 | 4 Aug | Infrastructure | Install Docker and Harbor on primary environment; record versions | Daniel Alexander | Manu Sasikanth Oruvilakode | Critical | Not started | P15-001 | Reproducible setup record |
| P15-008 | 2 | 4 Aug | Infrastructure | Establish a second independent Harbor environment for reproducibility | Mukesh Murugesan | Faisal Shoaib | High | Not started | P15-001 | Second-machine verification |
| P15-009 | 2 | 5 Aug | Benchmark | Run the official five-task oracle smoke test and archive results | Manh Tuan Nguyen | Yash Raj Singh | Critical | Not started | P15-007 | Harbor job output |
| P15-010 | 2 | 5 Aug | Mentor | Lead mentor discussion on model, baselines, resources, subset, and success definition | Manu Sasikanth Oruvilakode | Daniel Alexander | Critical | Not started | P15-006 | Confirmed minutes/decisions |
| P15-011 | 2 | 6 Aug | Cost/risk | Produce model/API/compute cost scenarios for development and full evaluation | Faisal Shoaib | Mukesh Murugesan | High | Not started | P15-010 | Cost model and recommendation |
| P15-012 | 2 | 6 Aug | Documentation | Update project assumptions, risk register, and task tracker after mentor meeting | Yash Raj Singh | Manh Tuan Nguyen | High | Not started | P15-010 | Approved tracker update |
| P15-013 | 3 | 10 Aug | Architecture | Define custom harness component boundaries and Harbor integration interface | Daniel Alexander | Faisal Shoaib | Critical | Not started | P15-010 | Architecture document/diagram |
| P15-014 | 3 | 10 Aug | Baselines | Pin established harness A version and configuration | Mukesh Murugesan | Yash Raj Singh | Critical | Not started | P15-010 | Baseline A config |
| P15-015 | 3 | 11 Aug | Baselines | Pin established harness B version and configuration | Manh Tuan Nguyen | Daniel Alexander | Critical | Not started | P15-010 | Baseline B config |
| P15-016 | 3 | 11 Aug | Experiment design | Select and freeze the 20-task development subset with rationale | Manu Sasikanth Oruvilakode | Mukesh Murugesan | Critical | Not started | P15-010 | Immutable task manifest |
| P15-017 | 3 | 12 Aug | Evaluation | Define metrics, failure taxonomy, rerun rules, and statistical approach | Faisal Shoaib | Manh Tuan Nguyen | Critical | Not started | P15-010 | Evaluation protocol |
| P15-018 | 3 | 12 Aug | Research integrity | Review contamination, oracle access, verifier, and validity controls | Yash Raj Singh | Manu Sasikanth Oruvilakode | High | Not started | P15-016, P15-017 | Validity checklist |
| P15-019 | 4 | 17 Aug | Baselines | Execute baseline A on the smoke set and development subset | Daniel Alexander | Manu Sasikanth Oruvilakode | Critical | Not started | P15-014, P15-016 | Saved jobs and result table |
| P15-020 | 4 | 17 Aug | Baselines | Execute baseline B on the smoke set and development subset | Mukesh Murugesan | Faisal Shoaib | Critical | Not started | P15-015, P15-016 | Saved jobs and result table |
| P15-021 | 4 | 18 Aug | Harness | Implement minimal external Harbor agent and terminal loop | Manh Tuan Nguyen | Yash Raj Singh | Critical | Not started | P15-013 | Tested custom skeleton |
| P15-022 | 4 | 18 Aug | Harness | Implement immutable configuration and structured trajectory logging | Manu Sasikanth Oruvilakode | Daniel Alexander | Critical | Not started | P15-013, P15-021 | Config schema and sample trajectory |
| P15-023 | 4 | 19 Aug | Analysis | Validate result extraction for accuracy, tokens, cost, runtime, and errors | Faisal Shoaib | Mukesh Murugesan | High | Not started | P15-019 to P15-022 | Reconciled result export |
| P15-024 | 5 | 26 Aug | Client | Build and deliver Week 5 early-progress evidence package and demonstration | Yash Raj Singh | Manh Tuan Nguyen | Critical | Not started | P15-019 to P15-023 | Slides, demo, minutes, feedback |
| P15-025 | 6 | 1 Sep | Harness | Establish the custom minimal baseline on the development subset | Daniel Alexander | Faisal Shoaib | Critical | Not started | P15-021 to P15-024 | Baseline jobs and summary |
| P15-026 | 6 | 1 Sep | Experiment | Compare direct prompting with staged inspect-plan-execute-verify prompting | Mukesh Murugesan | Yash Raj Singh | High | Not started | P15-025 | EX experiment record |
| P15-027 | 6 | 2 Sep | Experiment | Implement and test verification-gated completion | Manh Tuan Nguyen | Daniel Alexander | Critical | Not started | P15-025 | Ablation results and trajectories |
| P15-028 | 6 | 2 Sep | Experiment | Implement and test one evidence-guided repair attempt | Manu Sasikanth Oruvilakode | Mukesh Murugesan | High | Not started | P15-027 | Ablation results and trajectories |
| P15-029 | 7 | 8 Sep | Analysis | Classify baseline and custom-harness failures using the agreed taxonomy | Faisal Shoaib | Manh Tuan Nguyen | High | Not started | P15-025 to P15-028 | Reviewed failure dataset |
| P15-030 | 7 | 9 Sep | Client | Build and deliver midpoint comparison, demo, validity notes, and next experiments | Yash Raj Singh | Manu Sasikanth Oruvilakode | Critical | Not started | P15-026 to P15-029 | Slides, demo, minutes, actions |
| P15-031 | 8 | 15 Sep | Experiment | Compare full history with sliding-window context | Daniel Alexander | Manu Sasikanth Oruvilakode | High | Not started | P15-030 | Context ablation |
| P15-032 | 8 | 15 Sep | Experiment | Test state summary plus bounded recent observations | Mukesh Murugesan | Faisal Shoaib | High | Not started | P15-031 | Context ablation |
| P15-033 | 8 | 16 Sep | Experiment | Compare general shell interaction with selected structured tools | Manh Tuan Nguyen | Yash Raj Singh | Medium | Not started | P15-030 | Tool ablation |
| P15-034 | 8 | 16 Sep | Reliability | Add repetition, parser-error, and budget-exhaustion safeguards | Manu Sasikanth Oruvilakode | Daniel Alexander | High | Not started | P15-029 | Tests and reliability results |
| P15-035 | STUVAC | 23 Sep | Reproduction | Reproduce key winning and losing comparisons on the second environment | Faisal Shoaib | Mukesh Murugesan | Critical | Not started | P15-031 to P15-034 | Cross-environment result |
| P15-036 | STUVAC | 23 Sep | Report | Draft methods, architecture, experimental protocol, and early-results sections | Yash Raj Singh | Manh Tuan Nguyen | High | Not started | P15-025 to P15-035 | Report draft and citations |
| P15-037 | 9 | 28 Sep | Freeze | Prepare final configuration recommendation using the agreed selection rule | Daniel Alexander | Faisal Shoaib | Critical | Not started | P15-026 to P15-035 | Decision matrix |
| P15-038 | 9 | 29 Sep | Budget | Confirm full-run cost, provider capacity, concurrency, and rerun policy | Mukesh Murugesan | Yash Raj Singh | Critical | Not started | P15-037 | Approved run plan |
| P15-039 | 9 | 29 Sep | Reproducibility | Freeze dependencies, prompt, config, commit, tag, and artifact locations | Manh Tuan Nguyen | Daniel Alexander | Critical | Not started | P15-037 | Frozen release candidate |
| P15-040 | 9 | 30 Sep | Client | Lead pre-final meeting and record approval or required changes | Manu Sasikanth Oruvilakode | Mukesh Murugesan | Critical | Not started | P15-037 to P15-039 | Design-freeze minutes |
| P15-041 | 10 | 5 Oct | Evaluation | Execute final established-harness comparison under frozen conditions | Faisal Shoaib | Manh Tuan Nguyen | Critical | Not started | P15-040 | Final baseline jobs |
| P15-042 | 10 | 7 Oct | Evaluation | Execute final custom-harness evaluation and complete reruns allowed by protocol | Yash Raj Singh | Manu Sasikanth Oruvilakode | Critical | Not started | P15-040 | Final custom jobs |
| P15-043 | 11 | 12 Oct | Analysis | Produce statistical comparison, cost analysis, figures, and sensitivity checks | Daniel Alexander | Faisal Shoaib | Critical | Not started | P15-041, P15-042 | Reproducible analysis and figures |
| P15-044 | 11 | 12 Oct | Report | Integrate findings, limitations, validity threats, and recommendations | Mukesh Murugesan | Yash Raj Singh | Critical | Not started | P15-043 | Reviewed final report sections |
| P15-045 | 11 | 13 Oct | Presentation | Build presentation narrative and assign six speaking/Q&A roles | Manh Tuan Nguyen | Daniel Alexander | Critical | Not started | P15-043, P15-044 | Final slide deck |
| P15-046 | 11 | 14 Oct | Presentation | Run timed rehearsal, demo failure test, and backup-material review | Manu Sasikanth Oruvilakode | Mukesh Murugesan | Critical | Not started | P15-045 | Rehearsal record and backup demo |
| P15-047 | 12 | 20 Oct | Handover | Finalise repository, setup guide, result manifest, limitations, and client handover | Faisal Shoaib | Manh Tuan Nguyen | Critical | Not started | P15-041 to P15-046 | Reproducible handover package |
| P15-048 | 12 | 21 Oct | Showcase | Deliver showcase, record feedback, complete retrospective, and archive evidence | Yash Raj Singh | Manu Sasikanth Oruvilakode | Critical | Not started | P15-047 | Showcase evidence and retrospective |

## Initial ownership balance

| Member | Primary tasks | Count |
|---|---|---:|
| Daniel Alexander | P15-001, 007, 013, 019, 025, 031, 037, 043 | 8 |
| Mukesh Murugesan | P15-002, 008, 014, 020, 026, 032, 038, 044 | 8 |
| Manh Tuan Nguyen | P15-003, 009, 015, 021, 027, 033, 039, 045 | 8 |
| Manu Sasikanth Oruvilakode | P15-004, 010, 016, 022, 028, 034, 040, 046 | 8 |
| Faisal Shoaib | P15-005, 011, 017, 023, 029, 035, 041, 047 | 8 |
| Yash Raj Singh | P15-006, 012, 018, 024, 030, 036, 042, 048 | 8 |

Task counts are an initial structural check only. Review difficulty and estimated hours weekly.

## Weekly workload review

Complete this table during the weekly team meeting.

| Week | Member | Planned hours | Actual hours | Tasks done/in review | Review/meeting contribution | Next-week load | Rebalance action |
|---|---|---:|---:|---|---|---|---|
|  | Daniel Alexander |  |  |  |  |  |  |
|  | Mukesh Murugesan |  |  |  |  |  |  |
|  | Manh Tuan Nguyen |  |  |  |  |  |  |
|  | Manu Sasikanth Oruvilakode |  |  |  |  |  |  |
|  | Faisal Shoaib |  |  |  |  |  |  |
|  | Yash Raj Singh |  |  |  |  |  |  |

## Weekly close checklist

- [ ] Task statuses reflect reality.
- [ ] Every in-progress task has current evidence.
- [ ] Every blocked task identifies the blocker and escalation owner.
- [ ] Reviewers have accepted or returned submitted work.
- [ ] Each member updated their individual log.
- [ ] Planned and actual hours were discussed.
- [ ] Upcoming workload is reasonably balanced.
- [ ] Decisions were added to the meeting log.
- [ ] Experiments were added to the experiment register.
- [ ] Risks to the next client or assessment milestone were escalated.
