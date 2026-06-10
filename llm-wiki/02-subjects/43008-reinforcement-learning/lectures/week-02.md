---
type: lecture-note
subject: 43008-reinforcement-learning
week: 2
status: draft
---

# Week 02 - Multi-Armed Bandits and Exploration

## Source Files

- `sources/raw/43008 Reinforcement Learning/rl_slides/Week2-Lecture-2024.pdf` (pdf)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week2/Lab/UCB-illustration.pdf` (pdf)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week2/Lecture/Week2-Lecture-2024.pdf` (pdf)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week2/Lab/43008-Week2-MultiArmBandit-PartA-Solution.ipynb` (notebook)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week2/Lab/43008-Week2-MultiArmBandit-PartA.ipynb` (notebook)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week2/Lab/43008-Week2-MultiArmBandit-PartB-Solution.ipynb` (notebook)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week2/Lab/43008-Week2-MultiArmBandit-PartB.ipynb` (notebook)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week2/Lab/43008-Week2-MultiArmBandit-PartC-Solution.ipynb` (notebook)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week2/Lab/43008-Week2-MultiArmBandit-PartC.ipynb` (notebook)

## Working Summary

This is a first-pass curated note generated from copied module PDFs and notebooks. Verify details against the source files before using it for assessment.

## Study Objectives

- Explain exploration versus exploitation.
- Compare epsilon-greedy, UCB, and bandit evaluation ideas.
- Understand regret and action-value estimates.

## Likely Concepts

- agent-environment loop: The repeated interaction where an agent observes state, takes action, receives reward, and moves to a new state.
- exploration exploitation: The tradeoff between trying uncertain actions to learn and choosing actions believed to perform well.
- preference optimisation: Learning from preference comparisons or human feedback rather than only scalar environment rewards.
- value function: An estimate of expected return from a state or state-action pair under a policy or optimal behaviour.
- policy: A rule or model that maps states or observations to actions or action probabilities.
- actor critic: A method family that combines a policy model (actor) with a value estimator (critic).
- markov decision process: A formal model for sequential decision-making with states, actions, transition probabilities, and rewards.
- bellman equation: A recursive relationship that decomposes value into immediate reward plus discounted future value.
- partially observable mdp: An MDP variant where the agent does not fully observe the true state and must reason from observations or beliefs.
- policy iteration: A dynamic programming method that alternates policy evaluation and policy improvement.

## Extracted Keywords

- reward
- bandit
- algorithm
- problem
- each
- rewards
- average
- multi-arm
- epsilon-greedy
- environment
- time
- over

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
