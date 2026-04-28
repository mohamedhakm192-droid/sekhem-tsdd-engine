# SEKHEM-TSDD Autonomous Decision System

## Overview
SEKHEM-TSDD is a closed-loop, energy-constrained control architecture designed for real-time autonomous systems operating under uncertainty.

The system combines Lyapunov-based stability, barrier-function safety, and a reflex-based interrupt mechanism to ensure robust and safe operation under all 
---
## Simulation
<p align="center">
  <img src="docs/simulation.gif" width="100%">
</p>
---

## Key Properties
- Lyapunov stability (V̇ ≤ 0)
- Forward-invariant safety constraints (h_i(X) ≥ 0)
- Real-time safe operation
- Reflex-based fault tolerance
- Constraint-satisfying control via projection

---

## Core Idea
The system operates as a hybrid control architecture combining a decision loop with a fast interrupt reflex pathway.

---

## Mathematical Foundation
- Lyapunov function for stability
- Control Barrier Functions (CBFs) for safety
- Projection onto admissible control set

---

## Applications
- Autonomous systems  
- Multi-agent coordination  
- Safety-critical control systems  

---

## Author
Mohamed Abdelnaby
