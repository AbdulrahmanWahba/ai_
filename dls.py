
from puzzle import get_neighbors

def dls(start, goal, limit):
    stack = [(start, [], 0)]
    visited = set()

    while stack:
        state, path, depth = stack.pop()
        if state == goal:
            return path + [state]

        if depth < limit and state not in visited:
            visited.add(state)
            for n in get_neighbors(state):
                stack.append((n, path + [state], depth + 1))
    return None
