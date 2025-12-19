
from puzzle import get_neighbors, heuristic

def astar_list(start, goal):
  
    open_list = [(0, 0, start, [])]
    visited = set()

    while open_list:
       
        current_node = min(open_list, key=lambda x: x[0])
        
        open_list.remove(current_node)

        f, g, state, path = current_node

        if state == goal:
            return path + [state]

        if state not in visited:
            visited.add(state)
            for n in get_neighbors(state):
                new_g = g + 1
                new_f = new_g + heuristic(n, goal)
        
                open_list.append((new_f, new_g, n, path + [state]))
    return None
