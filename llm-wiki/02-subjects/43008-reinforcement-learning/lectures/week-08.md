---
type: lecture-note
subject: 43008-reinforcement-learning
week: 8
status: draft
---

# Week 08 - Function Approximation and Deep Q-Learning

## Source Files

- `sources/raw/43008 Reinforcement Learning/rl_slides/Week8-Lecture-2025.pdf` (pdf)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week8/Lecture/Week8-Lecture-2025.pdf` (pdf)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week8/Lab/2025/43008-Week8-Part-1-FA-Simple-Neural-Network-Solution-Colab.ipynb` (notebook)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week8/Lab/2025/43008-Week8-Part-C-SB3-Deep-Q-Network-Solution.ipynb` (notebook)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week8/Lab/2025/43008-Week8-TD-Methods-Part-B-DoubleQLearning-Gymnasium-Solution.ipynb` (notebook)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week8/Lab/2025/43008-Week8-TD-Methods-Part-B-DoubleQLearning_Gymnasium.ipynb` (notebook)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week8/Lab/43008-Week8-Part-1-FA-Simple-Neural-Network-Colab.ipynb` (notebook)
- `sources/raw/43008 Reinforcement Learning/viewer/files/Modules/Week8/Lab/CUDA,_Bias_and_Variance.ipynb` (notebook)

## Working Summary

This is a first-pass curated note generated from copied module PDFs and notebooks. Verify details against the source files before using it for assessment.

## Study Objectives

- Explain why function approximation is needed for large state spaces.
- Connect neural networks to value-function approximation.
- Understand Double Q-learning and DQN building blocks.

## Likely Concepts

- agent-environment loop: The repeated interaction where an agent observes state, takes action, receives reward, and moves to a new state.
- function approximation: Using parameterised models such as neural networks to estimate value functions or policies for large state spaces.
- value function: An estimate of expected return from a state or state-action pair under a policy or optimal behaviour.
- policy: A rule or model that maps states or observations to actions or action probabilities.
- q-learning: An off-policy temporal-difference control method for learning action-value estimates.
- deep q-network: A deep RL method that uses a neural network to approximate Q-values.
- exploration exploitation: The tradeoff between trying uncertain actions to learn and choosing actions believed to perform well.
- markov decision process: A formal model for sequential decision-making with states, actions, transition probabilities, and rewards.
- temporal difference learning: RL methods that update value estimates from bootstrapped predictions before an episode ends.
- actor critic: A method family that combines a policy model (actor) with a value estimator (critic).

## Extracted Keywords

- function
- import
- model
- environment
- approximation
- plot
- neural
- house
- layer
- using
- price
- code

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
