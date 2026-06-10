---
type: lecture-note
subject: 43008-reinforcement-learning
week: 3
status: draft
---

# Week 03 - MDPs and POMDPs

## Source Files

- `sources/raw/43008 Reinforcement Learning/rl_slides/Week3-Lecture-2024.pdf` (pdf)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week3/Lecture/Week3-Lecture-2024.pdf` (pdf)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week3/Lab/2024/43008-Week3-MDPs-CaseStudy-PartA-Solution.ipynb` (notebook)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week3/Lab/2024/43008-Week3-MDPs-CaseStudy-PartA.ipynb` (notebook)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week3/Lab/2024/43008-Week3-POMDPs-CaseStudy-PartA-Solution.ipynb` (notebook)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week3/Lab/2024/43008-Week3-POMDPs-CaseStudy-PartA.ipynb` (notebook)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week3/Lab/2024/43008-Week3-POMDPs-CaseStudy-PartB-Solution.ipynb` (notebook)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week3/Lab/2024/43008-Week3-POMDPs-CaseStudy-PartB.ipynb` (notebook)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week3/Lab/43008-Week3-MDPs-CaseStudy-PartB.ipynb` (notebook)

## Working Summary

This is a first-pass curated note generated from copied module PDFs and notebooks. Verify details against the source files before using it for assessment.

## Study Objectives

- Formulate sequential decision problems as MDPs.
- Explain state transitions, rewards, policies, and value functions.
- Recognise when partial observability changes the problem.

## Likely Concepts

- agent-environment loop: The repeated interaction where an agent observes state, takes action, receives reward, and moves to a new state.
- markov decision process: A formal model for sequential decision-making with states, actions, transition probabilities, and rewards.
- partially observable mdp: An MDP variant where the agent does not fully observe the true state and must reason from observations or beliefs.
- policy: A rule or model that maps states or observations to actions or action probabilities.
- value function: An estimate of expected return from a state or state-action pair under a policy or optimal behaviour.
- exploration exploitation: The tradeoff between trying uncertain actions to learn and choosing actions believed to perform well.

## Extracted Keywords

- pain
- current
- based
- rewards
- states
- location
- transition
- probabilities
- markov
- next
- scenario
- robot

## What To Understand

- What decision problem is being modelled.
- What the state, action, reward, and policy are.
- Whether the method is model-based, model-free, on-policy, or off-policy.
- How values, policies, or models are updated.
- What failure modes or evaluation issues matter.

## Assessment Relevance

- Link this week to assessment tasks involving algorithm explanation, implementation, or experiment analysis.
- Use notebook sources to verify algorithm steps and expected outputs.

## Revision Questions

- What problem does this RL method solve?
- What update equation or algorithm loop is central?
- What assumptions does the method make?
- How would you evaluate whether the learned policy is good?

## LLM Follow-Up Prompt

Using the source files listed above, expand this draft into a precise study note with definitions, equations, algorithm steps, notebook implementation details, and assessment relevance. Keep claims traceable to source files.
