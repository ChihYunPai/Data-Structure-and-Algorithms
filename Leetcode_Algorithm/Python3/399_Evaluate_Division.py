"""
Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0. 
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? . 
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.
"""
from queue import Queue
from collections import defaultdict
class Solution:
    
        
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        def findPath(graph, start, end, value=1.0):
            """
            BFS iterative
            """
            if start == end: return value
            queue = Queue()
            queue.put((start, 1.0))
            visited = set()
            while not queue.empty():
                node, value = queue.get()
                if node == end: return value
                visited.add(node)
                for child, v in graph[node]:
                    if child not in visited:
                        queue.put((child, value*v))
            return None
        
        assert(len(equations) == len(values))
        graph = defaultdict(list)
        for (e1, e2), v in zip(equations, values):
            graph[e1].append((e2, v))
            graph[e2].append((e1, 1.0/v))
        res = [-1.0]*len(queries)
        
        for i, (q1, q2) in enumerate(queries):
            if q1 not in graph or q2 not in graph: continue
            value = findPath(graph, q1, q2)
            if value != None:
                res[i] = value
        return res