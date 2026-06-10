---
type: lecture-note
subject: 43008-reinforcement-learning
week: 5
status: draft
---

# Week 05 - Value Iteration and Solving MDPs

## Source Files

- `sources/raw/43008 Reinforcement Learning/rl_slides/Week5-Lecture-2024.pdf` (pdf)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week5/Lecture/GridWorld-Illustration.pdf` (pdf)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week5/Lecture/Week5-Lecture-2024.pdf` (pdf)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week5/Lab/43008-Week5-MDPs-ValueIteration-Solution.ipynb` (notebook)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week5/Lab/43008-Week5-MDPs-ValueIteration.ipynb` (notebook)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week5/Lab/43008-Week5-SolvingMDPs-GYMNASIUM.ipynb` (notebook)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week5/Lab/GridWorld-Sutton-Barto-Chap04-V2-ClassBased.ipynb` (notebook)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week5/Lab/GridWorld-Sutton-Barto-Chap04.ipynb` (notebook)

## Working Summary

This is a first-pass curated note generated from copied module PDFs and notebooks. Verify details against the source files before using it for assessment.

## Study Objectives

- Explain Bellman optimality updates.
- Implement or trace value iteration.
- Connect gridworld examples to general MDP solution methods.

## Likely Concepts

- policy: A rule or model that maps states or observations to actions or action probabilities.
- agent-environment loop: The repeated interaction where an agent observes state, takes action, receives reward, and moves to a new state.
- policy iteration: A dynamic programming method that alternates policy evaluation and policy improvement.
- value function: An estimate of expected return from a state or state-action pair under a policy or optimal behaviour.
- markov decision process: A formal model for sequential decision-making with states, actions, transition probabilities, and rewards.
- value iteration: A dynamic programming method that repeatedly applies Bellman optimality updates to estimate optimal values.
- function approximation: Using parameterised models such as neural networks to estimate value functions or policies for large state spaces.
- actor critic: A method family that combines a policy model (actor) with a value estimator (critic).
- bellman equation: A recursive relationship that decomposes value into immediate reward plus discounted future value.

## Extracted Keywords

- random
- evaluation
- greedy
- function
- optimal
- iteration
- actions
- improvement
- algorithm
- policies
- shown
- import

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
