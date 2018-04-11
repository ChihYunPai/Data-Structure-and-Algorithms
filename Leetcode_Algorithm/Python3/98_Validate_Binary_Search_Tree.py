"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:
    2
   / \
  1   3
Binary tree [2,1,3], return true.
Example 2:
    1
   / \
  2   3
Binary tree [1,2,3], return false.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Better version and more concise
"""
import sys
class Solution:
	"""
	Time: O(n)
	Space: O(n)
	"""
    MIN = -sys.maxsize
    MAX = sys.maxsize
    def _isBST(self, node, min, max):
        if not node:
            return True
        if not (min < node.val < max):
            return False
        return self._isBST(node.left, min, node.val) and self._isBST(node.right, node.val, max)
    
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self._isBST(root, self.MIN, self.MAX)


# import sys
# class Solution:
# 	"""
# 	Time: O(n)
# 	Space: O(n)
# 	"""
#     MIN = -sys.maxsize
#     MAX = sys.maxsize
#     def _isBST(self, node):
#         if not node.left and not node.right:
#             return (node.val, node.val)
#         l_min = r_min = self.MAX
#         l_max = r_max = self.MIN
#         if node.left:
#             (l_min, l_max) = self._isBST(node.left)
#             if max(l_min, l_max) >= node.val:
#                 return (self.MIN, self.MAX)
#         if node.right:
#             (r_min, r_max) = self._isBST(node.right)
#             if min(r_min, r_max) <= node.val:
#                     return (self.MIN, self.MAX)
#         return (min([node.val, l_min, r_min]), max([node.val, l_max, r_max]))
    
#     def isValidBST(self, root):
#         """
#         :type root: TreeNode
#         :rtype: bool
#         """
#         if not root:
#             return True
#         if not root.left and not root.right:
#             return True
#         if root.left:
#             (l_min, l_max) = self._isBST(root.left)
#             if l_max >= root.val:
#                 return False
#         if root.right:
#             (r_min, r_max) = self._isBST(root.right)
#             if r_min <= root.val:
#                 return False
#         return True