from dls import dls

def ids(start, goal, max_depth=50):
    for depth in range(max_depth + 1):
        result = dls(start, goal, depth)
        if result is not None:
            return result
    return None
