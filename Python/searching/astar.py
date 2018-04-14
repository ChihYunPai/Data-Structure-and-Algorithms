"""
Implementation of A* Search
"""
from queue import PriorityQueue as PQueue
from collections import defaultdict

cost = defaultdict(dict) # cost[x][y] contains the cost from node x to y
def c(start, end):
	# return cost from start to end
	return cost[start][end]

def h(start, end, heristicFunc=EuclideanDistance):
	# return heuristic cost estimation from start to end
	return fuc(start, end)

def path(cameFrom, node):
	path = [node]
	while not in cameFrom.keys():
		node = cameFrom[node]
		p.insert(0, node)
	return path

def Astar(problem):
	start = problem.sart
	goal = problem.goal
    visited = set()
    toVisit = PQueue()
    cameFrom = {}
    f = defaultdict(lambda: float('inf'))
    g = defaultdict(lambda: float('inf'))
    g[start] = 0
    f[start] = g[start] + h(start, goal)
    toVisit.put((f[start], start))

    while not toVisit.empty():
    	f_score, node = toVisit.get()
    	if node == goal:
    		return path(cameFrom, node)
    		visited.add(node)
    		for child in graph[node]:
    			tentative_score = g[node] + c[node][child]
    			if tentative_score < g[child]:
    				g[child] = tentative_score
    				f[child] = g[child] + h(child, goal)
    				cameFrom[child] = node
    return None # not found any path