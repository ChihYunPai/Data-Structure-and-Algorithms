"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __traverse(self, root, lst=[], h=1):
        if not root:
            return
        lst.append((root.val, h))
        self.__traverse(root.left, lst, h+1)
        self.__traverse(root.right, lst, h+1)
        
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        lst = []
        self.__traverse(root, lst)
        heights = sorted(list(set(map(lambda x: x[1], lst))), reverse=True)
        return [[x[0] for x in lst if x[1] == height] for height in heights]