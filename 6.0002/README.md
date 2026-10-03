# MIT 6.0002 — Introduction to Computational Thinking and Data Science

Self-study through MIT 6.0002 (Fall 2016), focusing on optimization, graph algorithms, stochastic simulation, and data analysis in Python.

## Problem Sets

| Problem Set | Topics |
|-------------|--------|
| PS1 | Space Cows transportation: greedy algorithms, brute-force search, and dynamic programming |
| PS2 | Fastest Way to Get Around MIT: weighted directed graphs and depth-first search with total-distance and outdoor-distance constraints |
| PS3 | Robot Simulation: object-oriented design, Monte Carlo simulation, and random-walk movement models |

> **Note:** Future coursework (PS4: disease and bacteria population simulation, PS5: modeling global warming) will be added here as the self-study progresses.

## Reflections

Writing the robot simulation made the difference between a deterministic algorithm and a stochastic one concrete. My first version of the robot's movement function looped until it found a valid move, which froze the visualization. Rewriting it so each time step makes a single attempt and turns in a new random direction if blocked fixed the hang and matched how a random walk actually works. Running many independent trials and averaging the results is what turns one noisy run into a reliable estimate.
