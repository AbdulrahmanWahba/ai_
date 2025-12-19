
import random
from puzzle import get_neighbors, heuristic

def hill_climbing(start, goal, max_iter=50000):
    current = start
    path = [current]
    visited = {current}
    
    for _ in range(max_iter):
        if current == goal:
            return path
        
        neighbors = get_neighbors(current)
        
        best_h = float('inf')
        candidates = []
        
        for neighbor in neighbors:
            if neighbor in visited:
                continue
                
            h = heuristic(neighbor, goal)
            if h < best_h:
                best_h = h
                candidates = [neighbor]
            elif h == best_h:
                candidates.append(neighbor)
        
        if not candidates:
             return None
             
        current = random.choice(candidates)
        visited.add(current)
        path.append(current)

    return None
