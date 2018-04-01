"""
Implementation of Depth First Search
"""
from queue import LifoQueue as Stack


def dfs(problem):
    open_set = Stack() # LIFO open_set
    closed_set = set() # visited nodes set
    meta = dict() # meat information, meta[key] = (parent_state, action to reach child)

    # Initialize
    root = problem.get_root()
    meta[root] = (None, None)
    open_set.put(root)

    while not open_set.empty():
        node = open_set.get()
        if problem.isGoal(node):
            return construc_path(node, meta)
        for (child, action) in problem.getSuccessors(node):
            if child in closed_set:
                continue
            if child not in open_set:
                meta[child] = (node, action)
                open_set.put(child)
        closed_set.add(node)

def construct_path(state, meta):
    action_list = list()
    while True:
        row = meta[state]
        if len(row) == 2:
            state, action = row[0], row[1]
            action_list.append(action)
        else:
            break
    return action_list[::-1]