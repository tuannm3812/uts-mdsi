# Project 15 Workspace

## Project

**Build a Custom Harness and Beat an Established One on Terminal-Bench**

The team will compare two established agent harnesses with a custom harness while holding the model and benchmark conditions constant. Development will use a frozen 20-task subset. The final design will be evaluated on all 89 Terminal-Bench 2.1 tasks if the confirmed compute and API budget permits.

## Current status

- Team: **Team iLab 15-1**, confirmed 2 Aug 2026 — Daniel Alexander, Mukesh Murugesan, Manh Tuan Nguyen, Manu Sasikanth Oruvilakode, Faisal Shoaib, Yash Raj Singh
- Mentor: **William Feng** (MDSI alumni 2023, Telstra Data Insights Analyst, ~2.5 yrs iLab mentoring) — made first contact 2 Aug 2026 via Teams; weekly 30-min catchup, Wednesdays, exact slot TBD
- Client/brief author: **William So**, Synogize — do not conflate with the mentor
- Team leader: **Manh Tuan Nguyen**
- MS Teams timeslot: Wednesday **6:30-7:00pm** (Team iLab 15-1)
- Group name: pending
- Work allocation: three pairs with rotating secondary responsibilities
- Model: awaiting mentor/client confirmation
- Established harnesses: awaiting mentor/client confirmation
- API/compute funding: awaiting mentor/client confirmation
- Development subset: awaiting mentor/client confirmation or approval

## Project resources

- [Official brief (verbatim)](official-brief-verbatim.md) — the authoritative Project 15 source text, extracted 4 Aug 2026
- [Agent collaboration log](agent-collaboration-log.md) — open running discussion between Tuan, Claude, and Codex
- [Detailed literature review](../research/project-15-terminal-bench-literature-review.md)
- [PDF literature review](../research/project-15-terminal-bench-literature-review.pdf)
- [Vietnamese literature review](../research/project-15-terminal-bench-literature-review-vi.md)
- [Vietnamese PDF literature review](../research/project-15-terminal-bench-literature-review-vi.pdf)
- [Team task tracker](team-task-tracker.md)
- [Individual contribution log template](individual-contribution-log-template.md)
- [Experiment register](experiment-register.md)
- [Meeting and decision log](meeting-and-decision-log.md)
- [Capstone topic brief](../sources/capstone-topic-picker-2026.md)
- [Kickoff requirements](../sources/36127-kickoff-requirements-spring-2026.md)

## Workstreams

| Pair | Members | Primary workstream | Rotating secondary work |
|---|---|---|---|
| A | Daniel Alexander and Mukesh Murugesan | Harbor environment and established baselines | Literature synthesis, report review, presentation |
| B | Manh Tuan Nguyen and Manu Sasikanth Oruvilakode | Custom harness and agent behaviour | Experiment review, client demonstrations, documentation |
| C | Faisal Shoaib and Yash Raj Singh | Evaluation, analysis, and documentation | Test automation, reproducibility review, integration |

Primary ownership gives one person accountability for delivery. It does not mean that person works alone. Every task has a reviewer, and pairs should cross-train so that no critical component has a single point of failure.

## Status vocabulary

| Status | Meaning |
|---|---|
| Not started | Accepted but work has not begun |
| Ready | Dependencies are complete and the task can start |
| In progress | Active work exists with an owner and evidence |
| In review | Deliverable is ready for its named reviewer |
| Blocked | A documented dependency or decision prevents progress |
| Done | Definition of done is satisfied and evidence is linked |
| Deferred | Intentionally removed from the current milestone with a recorded reason |

## Definition of done

A task is done only when:

1. the stated deliverable exists;
2. relevant checks pass;
3. the reviewer has inspected it;
4. assumptions, configuration, and limitations are documented;
5. evidence is linked from the tracker;
6. decisions affecting later work are recorded; and
7. the owner updates their individual weekly log.

## Evidence standard

Useful evidence includes:

- GitHub issue or task ID;
- commit or pull request;
- experiment configuration and result directory;
- notebook, analysis, or figure;
- test output;
- meeting minutes and decisions;
- client/mentor feedback;
- report edit history; and
- presentation slides or rehearsal notes.

Evidence should show both the work and the student's role. A message saying “completed” without an artifact or review trail is not strong evidence.

## Weekly operating routine

### Before the team meeting

- Update task status and evidence links.
- Update the individual contribution log.
- Record blockers and decisions required.
- Compare planned and actual hours.

### During the team meeting

- Review the next milestone.
- Check workload across all six members.
- Resolve or escalate blockers.
- Review experiment validity and cost.
- Assign one owner and one reviewer to every new task.
- Record decisions and actions in the meeting log.

### After the team meeting

- Confirm due dates and dependencies.
- Create or update GitHub issues.
- Share minutes in Slack.
- Escalate mentor/client questions promptly.

## Workload balancing

The initial tracker allocates eight primary tasks to each member. Equality must also consider task difficulty, approximate hours, reviews, meetings, writing, and presentation work. Rebalance weekly when:

- one member's estimated workload differs materially from the group;
- a blocked member can support another workstream;
- a member repeatedly performs invisible coordination work;
- one technical component depends on a single person; or
- a deadline changes the relative urgency of tasks.

## Git workflow

- Use one issue or task ID for every meaningful deliverable.
- Create focused branches and pull requests for technical work.
- Include the task ID in commit and pull-request descriptions.
- Require at least one reviewer.
- Do not commit API keys, secrets, raw provider credentials, or private client data.
- Tag frozen baseline and final-evaluation configurations.
