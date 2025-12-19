
import heapq
from puzzle import get_neighbors,heuristic


def astar(start, goal):
    pq = [(0, 0, start, [])]
    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)
        if state == goal:
            return path + [state]

        if state not in visited:
            visited.add(state)
            for n in get_neighbors(state):
                new_g = g + 1
                new_f = new_g + heuristic(n, goal)
                heapq.heappush(pq, (new_f, new_g, n, path + [state]))
    return None
