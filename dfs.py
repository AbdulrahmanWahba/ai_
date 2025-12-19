from puzzle import get_neighbors

def dfs(start, goal, max_depth=50):
    stack = [(start, [], 0)]
    visited = {}

    while stack:
        state, path, depth = stack.pop()

        if state == goal:
            return path + [state]

        if depth >= max_depth:
            continue
            
        if state in visited and visited[state] <= depth:
            continue
        visited[state] = depth

        neighbors = get_neighbors(state)
        

        for n in neighbors:
            stack.append((n, path + [state], depth + 1))
            
    return None
