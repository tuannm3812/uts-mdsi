---
type: glossary
subject: 43008-reinforcement-learning
status: draft
---

# 43008 Reinforcement Learning - Glossary

| Term | Evidence Count | Working Definition |
|---|---:|---|
| agent-environment loop | 2857 | The repeated interaction where an agent observes state, takes action, receives reward, and moves to a new state. |
| policy | 810 | A rule or model that maps states or observations to actions or action probabilities. |
| value function | 382 | An estimate of expected return from a state or state-action pair under a policy or optimal behaviour. |
| exploration exploitation | 369 | The tradeoff between trying uncertain actions to learn and choosing actions believed to perform well. |
| markov decision process | 277 | A formal model for sequential decision-making with states, actions, transition probabilities, and rewards. |
| preference optimisation | 203 | Learning from preference comparisons or human feedback rather than only scalar environment rewards. |
| policy iteration | 184 | A dynamic programming method that alternates policy evaluation and policy improvement. |
| function approximation | 162 | Using parameterised models such as neural networks to estimate value functions or policies for large state spaces. |
| actor critic | 113 | A method family that combines a policy model (actor) with a value estimator (critic). |
| hierarchical reinforcement learning | 111 | RL methods that organise decisions into higher-level skills, options, or subtasks. |
| monte carlo methods | 101 | Sampling-based RL methods that estimate values from complete episodes. |
| temporal difference learning | 67 | RL methods that update value estimates from bootstrapped predictions before an episode ends. |
| q-learning | 66 | An off-policy temporal-difference control method for learning action-value estimates. |
| deep q-network | 65 | A deep RL method that uses a neural network to approximate Q-values. |
| bellman equation | 46 | A recursive relationship that decomposes value into immediate reward plus discounted future value. |
| partially observable mdp | 41 | An MDP variant where the agent does not fully observe the true state and must reason from observations or beliefs. |
| monte carlo tree search | 24 | A planning method that uses simulated rollouts to estimate promising actions in a search tree. |
| value iteration | 20 | A dynamic programming method that repeatedly applies Bellman optimality updates to estimate optimal values. |

## Maintenance

- Replace working definitions with precise definitions and equations from lectures.
- Link durable terms to [Reinforcement Learning](../../03-shared-concepts/reinforcement-learning.md), [Artificial Intelligence](../../03-shared-concepts/artificial-intelligence.md), and [Machine Learning](../../03-shared-concepts/machine-learning.md).
