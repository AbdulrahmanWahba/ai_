
from collections import deque
from puzzle import get_neighbors

def bfs(start, goal):
    queue = deque([(start, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path + [state]

        if state not in visited:
            visited.add(state)
            for n in get_neighbors(state):
                queue.append((n, path + [state]))
    return None
