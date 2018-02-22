"""
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:
Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


###############################################
# FIRST VERSION
###############################################
# class Solution:
#     import sys
#     __diff = sys.maxsize
#     __closestValue = 0
    
#     def findTarget(self, root, target):
#         if root==None: 
#             return
#         curr_diff = abs(root.val - target)
#         if self.__diff > curr_diff:
#             self.__diff = curr_diff
#             self.__closestValue = root.val
#         if target < float(root.val):
#             self.findTarget(root.left, target)
#         else:
#             self.findTarget(root.right, target)
    
#     def closestValue(self, root, target):
#         """
#         :type root: TreeNode
#         :type target: float
#         :rtype: int
#         """
#         if root==None:
#             return 0
#         self.findTarget(root, target)
#         return self.__closestValue

class Solution:
    
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        nextNode = root.left if target < root.val else root.right
        if not nextNode: return root.val
        nextValue = self.closestValue(nextNode, target)
        return min((root.val, nextValue), key=lambda x: abs(x - target))