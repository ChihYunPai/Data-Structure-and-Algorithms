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


def dfs(graph, start, goal):
    visited = set()
    stack = Stack()
    stack.put(start)

    while not stack.empty():
        node = stack.get()
        if node == goal:
            return True
        visited.add(node)
        for child in graph[node]:
            if child not in visited:
                stack.put(child)
    return False

def bfs(graph, start, goal):
    visited = set()
    queue = Queue()
    queue.put(start)

    while not queue.empty():
        node  = queue.get()
        if node == goal:
            return True
        visited.add(node)
        for child in graph[node]:
            if child not in visited:
                queue.put(child)
    return False

def astar(graph, start, goal, h):
    visited = set()
    pqueue = PQueue()
    pqueue.put((0, start))
    g = defaultdict(int)
    f = defaultdict(int)
    g[start] = 0
    f[start] = g[(start, start)] + h(start, goal)

    while not pqueue.empty():
        f_score, node = pqueue.get()
        if node == goal:
            return path(camFrom, node)


        if node == goal:
            return True
        visited.add(node)
        for child in graph[node]:
            curr = g[] + h
            
def path(cameFrom, node):
    path = [node]
    while node in cameFrom.keys():
        node = cameFrom[node[]
        path.insert(0, node)




visited = set() # or visited = [False] * len(nodes)

pqueue = PQueue()
pqueue.put((0, start))
while not pqueue.empty():
    _, node = pqueue.get()
    if node == goal: return True
    visited.add(node)
    for child in graph[node]:
        # if not visited[node]:

        if node not in visited:
            pqueue.put((f))

