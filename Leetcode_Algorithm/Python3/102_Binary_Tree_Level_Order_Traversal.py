"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Queue:
    def __init__(self):
        self.queue = []
        
    def __str__(self):
        string = ""
        for x in self.queue:
            string += (str(x) + " ")
        return string
        
    def push(self, obj):
        self.queue.append(obj)
        
    def pop(self):
        return self.queue.pop(0)
    
    def empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
class Solution:
    
    def __traverse(self, root, queue, h=1):
        if not root:
            return
        queue.push((root.val, h))
        self.__traverse(root.left, queue, h+1)
        self.__traverse(root.right, queue, h+1)
        
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        queue = Queue()
        self.__traverse(root, queue)
        heights = set(map(lambda x: x[1], queue.queue))
        return [[x[0] for x in queue.queue if x[1]==height] for height in heights]