"""
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

For example:

Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.

Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.

Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

"""
from queue import LifoQueue as Stack
from collections import defaultdict
class Solution:
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges) != n-1:
            return False
        
        dic = defaultdict(list)
        for x, y in edges:
        	assert(isinstance(x, int) and isinstance(y, int))
            dic[x].append(y)
            dic[y].append(x)
        stack = Stack()
        stack.put(0)
        visited = set([0])
        while not stack.empty():
            node = stack.get()
            visited.add(node)
            for child in dic[node]:
                if child not in visited:
                    stack.put(child)
        return len(visited) == n