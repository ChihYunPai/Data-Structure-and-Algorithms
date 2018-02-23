"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
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
        self.lst = []
        
    def __str__(self):
        string = ""
        for x in self.lst:
            string += (str(x) + " ")
        return string
    
    def __len__(self):
        return len(self.lst)
    
    def empty(self):
        return len(self)==0
    
    def pop(self):
        return self.lst.pop(0)
    
    def push(self, obj):
        self.lst.append(obj)
        
class Solution:
    
    def __traverse(self, root, queue, h=1):
        if not root: return
        queue.push((root.val, h))
        self.__traverse(root.left, queue, h+1)
        self.__traverse(root.right, queue, h+1)
        
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        queue = Queue()
        self.__traverse(root, queue)
        heights = set([x[1] for x in queue.lst])
        lst = [[x[0] for x in queue.lst if x[1]==height] for height in heights]
        
        for (i, subList) in enumerate(lst):
            if i%2 == 1:
                lst[i] = lst[i][::-1]
        return lst
        