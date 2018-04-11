"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
"""
class CLList():
        def __init__(self, i):
            self.i = i
            self.next = None
            
class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        """
        Time: O(n)
        Space: O(n)
        """
        if len(matrix) == 0: return []
        if len(matrix[0]) == 0: return []
        m, n = len(matrix), len(matrix[0])
        size = m*n
        graph = {}
        for i in range(m):
            for j in range(n):
                graph[(i, j)] = [None if j == n-1 else (i, j+1),
                                 None if i == m-1 else (i+1, j),
                                 None if j == 0   else (i, j-1),
                                 None if j == n-1 else (i-1, j)]
        # initialize list
        dir = CLList(0)
        start = dir
        for i in range(1, 4):
            dir.next = CLList(i)
            dir = dir.next
        dir.next = start
        dir = dir.next
        
        # initialization
        visited = set()
        node = (0, 0)
        res = [0] * size
        i = 0
        
        # process
        while len(visited) < size:
            visited.add(node)
            res[i] = matrix[node[0]][node[1]]
            i += 1
            next_node = graph[node][dir.i]
            if next_node == None or next_node in visited:
                dir = dir.next
                next_node = graph[node][dir.i]
            node = next_node
        return res