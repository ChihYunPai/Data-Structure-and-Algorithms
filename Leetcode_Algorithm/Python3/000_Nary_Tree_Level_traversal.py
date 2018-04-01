"""
Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example, given a 3-ary tree:





We should return its level order traversal:

[
     [1],
     [3,2,4],
     [5,6]
]
Note:
The depth of the tree is at most 1000.
The total number of nodes is at most 5000.
"""
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ans = [[]]
        prev = 1
        queue = [(1, root)]
        while len(queue):
            depth, node = queue.pop(0)
            if depth == prev:
                ans[-1].append(node.val)
            else:
                ans.append([node.val])
                prev += 1
            for child in node.children:
                queue.append((depth + 1, child))
        return ans
            
        
        
