"""
Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None: return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

################################################################
# class Solution:
#     def __countLeft(self, root):
#         if root == None:
#             return 1
#         return 1 + self.__countLeft(root.left)
    
#     def __countRight(self, root):
#         if root == None:
#             return 1
#         return 1 + self.__countRight(root.right)
    
#     def countNodes(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         if root == None: 
#             return 0
#         leftHeight = self.__countLeft(root.left)
#         rightHeight = self.__countRight(root.right)
        
#         if leftHeight == rightHeight:
#             return (2**leftHeight - 1)
#         return 1 + self.countNodes(root.left) + self.countNodes(root.right)