---
type: lecture-note
subject: 43008-reinforcement-learning
week: 4
status: draft
---

# Week 04 - Policy Iteration

## Source Files

- `sources/raw/43008 Reinforcement Learning/rl_slides/Week4-Lecture-2024.pdf` (pdf)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week4/Lecture/Policy Iteration Algorithm.pdf` (pdf)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week4/Lecture/Week4-Lecture-2024.pdf` (pdf)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week4/Lab/43008-Week4-MDPs-PolicyIteration-OpenAI-Gym-Solution.ipynb` (notebook)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week4/Lab/43008-Week4-MDPs-PolicyIteration-Solution.ipynb` (notebook)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week4/Lab/43008-Week4-MDPs-PolicyIteration.ipynb` (notebook)

## Working Summary

This is a first-pass curated note generated from copied module PDFs and notebooks. Verify details against the source files before using it for assessment.

## Study Objectives

- Explain policy evaluation and policy improvement.
- Trace policy iteration step by step.
- Understand convergence intuition for dynamic programming methods.

## Likely Concepts

- agent-environment loop: The repeated interaction where an agent observes state, takes action, receives reward, and moves to a new state.
- policy: A rule or model that maps states or observations to actions or action probabilities.
- value function: An estimate of expected return from a state or state-action pair under a policy or optimal behaviour.
- policy iteration: A dynamic programming method that alternates policy evaluation and policy improvement.
- bellman equation: A recursive relationship that decomposes value into immediate reward plus discounted future value.
- markov decision process: A formal model for sequential decision-making with states, actions, transition probabilities, and rewards.

## Extracted Keywords

- function
- rewards
- next
- bellman
- each
- state-value
- reward
- current
- update
- transition
- iteration
- best

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
