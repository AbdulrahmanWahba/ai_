
import heapq
from puzzle import get_neighbors

def ucs(start, goal):
    pq = [(0, start, [])]
    visited = set()

    while pq:
        cost, state, path = heapq.heappop(pq)
        if state == goal:
            return path + [state]

        if state not in visited:
            visited.add(state)
            for n in get_neighbors(state):
                heapq.heappush(pq, (cost + 1, n, path + [state]))
    return None
