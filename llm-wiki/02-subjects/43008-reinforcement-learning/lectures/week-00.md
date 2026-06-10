---
type: lecture-note
subject: 43008-reinforcement-learning
week: 0
status: draft
---

# Week 00 - Mathematical and Probability Prerequisites

## Source Files

- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week0/RLbook2020.pdf` (pdf)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week0/cs229-LinearAlgebra-Review.pdf` (pdf)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week0/cs229-probability.pdf` (pdf)

## Working Summary

This is a first-pass curated note generated from copied module PDFs and notebooks. Verify details against the source files before using it for assessment.

## Study Objectives

- Review linear algebra and probability notation used by RL algorithms.
- Understand why expectation, value, and optimisation appear throughout RL.

## Likely Concepts

- policy: A rule or model that maps states or observations to actions or action probabilities.
- function approximation: Using parameterised models such as neural networks to estimate value functions or policies for large state spaces.
- agent-environment loop: The repeated interaction where an agent observes state, takes action, receives reward, and moves to a new state.
- temporal difference learning: RL methods that update value estimates from bootstrapped predictions before an episode ends.
- monte carlo methods: Sampling-based RL methods that estimate values from complete episodes.
- actor critic: A method family that combines a policy model (actor) with a value estimator (critic).
- value function: An estimate of expected return from a state or state-action pair under a policy or optimal behaviour.
- exploration exploitation: The tradeoff between trying uncertain actions to learn and choosing actions believed to perform well.
- policy iteration: A dynamic programming method that alternates policy evaluation and policy improvement.
- bellman equation: A recursive relationship that decomposes value into immediate reward plus discounted future value.

## Extracted Keywords

- random
- probability
- matrix
- variable
- multiplication
- example
- variables
- product
- methods
- properties
- case
- vector

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
