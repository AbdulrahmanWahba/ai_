# 🧩 8-Puzzle AI Project – Report 

## Introduction

The 8-Puzzle is a well-known problem in the field of Artificial Intelligence. It consists of a **3×3 grid** containing eight numbered tiles and one empty space. The tiles can be moved by sliding them into the empty space. The main objective is to transform an initial configuration into a predefined goal configuration using the smallest number of moves.

This project demonstrates how different **AI search algorithms** can be applied to solve the 8-Puzzle problem and highlights the strengths and weaknesses of each algorithm.

---

## Project Objectives

* Implement multiple AI search algorithms to solve the 8-Puzzle problem.
* Understand how each algorithm explores the state space.
* Compare algorithms based on solution optimality, speed, and memory usage.
* Provide a clear and simple implementation suitable for academic purposes.

---

## Algorithms Implemented

### 1️⃣ Breadth-First Search (BFS)

* Explores all states at the same depth before moving to deeper levels.
* Guarantees finding the shortest path to the goal.
* Requires a large amount of memory due to storing all frontier nodes.

---

### 2️⃣ Depth-First Search (DFS)

* Explores one branch deeply before backtracking.
* Uses less memory compared to BFS.
* Does not guarantee the shortest solution and may take longer in some cases.

---

### 3️⃣ Depth-Limited Search (DLS)

* A variation of DFS with a predetermined depth limit.
* Prevents DFS from exploring too deep or getting stuck in infinite loops.
* If the goal is not found within the limit, it returns no solution (for that limit).

---

### 4️⃣ Uniform Cost Search (UCS)

* Expands the node with the lowest cumulative path cost.
* Guarantees an optimal solution when step costs are uniform.
* More systematic than DFS but slower than heuristic-based methods.

---

### 5️⃣ Hill Climbing

* A local search algorithm that iteratively moves to a better neighbor.
* Uses a heuristic function (Manhattan Distance) to evaluate states.
* fast and uses little memory.
* **Enhancement**: Implements **Enforced Hill Climbing** (by tracking visited states) to force exploration of new states even if they have higher heuristic cost, preventing infinite loops and local optima.
* **Drawback**: Can produce long, non-optimal paths.

---

### 6️⃣ A* Search Algorithm

* Combines path cost (g) and heuristic cost (h).
* Efficient and optimal when using an admissible heuristic.
* Generally provides the best performance for the 8-Puzzle problem.
* Common heuristic used: **Manhattan Distance**.

---

## Project Structure

```
8-Puzzle-AI/
│
├── main.py              # Main program (algorithm selection)
├── puzzle.py            # State representation, moves, and heuristic
│
├── bfs.py               # Breadth-First Search implementation
├── dfs.py               # Depth-First Search implementation
├── dls.py               # Depth-Limited Search implementation
├── ucs.py               # Uniform Cost Search implementation
├── hill_climbing.py     # Hill Climbing implementation
├── astar.py             # A* Search implementation
│
└── README.md
```

---

## Performance Comparison

* **BFS** ensures the shortest solution but requires high memory.
* **DFS** reduces memory usage but may not produce an optimal solution.
* **DLS** offers memory efficiency like DFS but avoids infinite depth issues.
* **UCS** guarantees optimality but is computationally expensive.
* **Hill Climbing** is very fast but risks getting stuck in local optima.
* **A*** provides a balanced and efficient approach by combining cost and heuristic information.

The comparison clearly shows why heuristic-based algorithms, especially A*, are preferred for complex search problems.


👥 Team Members
 
* Abdelrahman mohamed wahba
* Omar hamdy mabrok
* Marwan maher elnahal
* Yousef ahmed mossad
* Ahmed aboelmagd kandel
* Hazem mohamed elbably