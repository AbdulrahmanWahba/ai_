
from bfs import bfs
from dfs import dfs
from dls import dls
from ucs import ucs
from hill_climbing import hill_climbing
from astar import astar
from ids import ids



def print_state(state):
    for row in state:
        print(*row)

start_state = (
   (1,2,3),
    (4,0,5),
    (6,7,8)
)

goal_state = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 0)
)

print("8 Puzzle Game")
print("1 - BFS")
print("2 - DFS")
print("3 - DLS")
print("4 - UCS")
print("5 - Hill Climbing")
print("6 - A*")
print("7 - IDS")


choice = input("Choose algorithm: ")

if choice == "1":
    solution = bfs(start_state, goal_state)
elif choice == "2":
    solution = dfs(start_state, goal_state)
elif choice == "3":
    limit = int(input("Enter depth limit: "))
    solution = dls(start_state, goal_state, limit)
elif choice == "4":
    solution = ucs(start_state, goal_state)
elif choice == "5":
    solution = hill_climbing(start_state, goal_state)
elif choice == "6":
    solution = astar(start_state, goal_state)
elif choice == "7":
    solution = ids(start_state, goal_state)
else:
    solution = None

if solution is not None or (solution is None and choice not in ["1", "2", "3", "4", "5", "6", "7"]):
    print("\nSolution:")
    if solution:
       step_number = 0
       for step in solution:
        print(f"Step {step_number}:")
        print_state(step)
        print("-" * 10)
        step_number += 1
    
    else:
        print("No solution found")
