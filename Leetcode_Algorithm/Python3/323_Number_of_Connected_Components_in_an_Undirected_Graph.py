"""
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

Example 1:
     0          3
     |          |
     1 --- 2    4
Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.

Example 2:
     0           4
     |           |
     1 --- 2 --- 3
Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]], return 1.

Note:
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.


"""

from collections import defaultdict
from queue import LifoQueue as Stack
from queue import Queue
class Solution:
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        """
        Time: O(n)
        Space: O(n)
        """
        # input validation
        assert(0 <= len(edges))
        assert(isinstance(n, int))
        
        if n == 0:
            return 0
        if len(edges) == 0:
            return n
        
        # initialization
        graph = defaultdict(list)
        count = 0
        visited = [False]*n
        for vi, vj in edges:
            graph[vi].append(vj)
            graph[vj].append(vi)
            
        for i in range(n):
            if not visited[i]:
                count += 1
                stack = Stack()
                stack.put(i)
                while not stack.empty():
                    node = stack.get()
                    visited[node] = True
                    for x in graph[node]:
                        if not visited[x]:
                            stack.put(x)
        return count
                