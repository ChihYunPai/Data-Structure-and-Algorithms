"""
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
First brute force version
Time: O(n logn)
Space: O(n)
"""
# class Solution:
#     def _traverse(self, node, lst):
#         if not node:
#             return
#         if node.right:
#             self._traverse(node.right, lst)
#         if node.left:
#             self._traverse(node.left, lst)
#         lst.append(node.val)
        
#     def _change(self, node, lst):
#         if not node:
#             return
#         if node.right:
#             self._change(node.right, lst)
#         if node.left:
#             self._change(node.left, lst)
#         node.val += sum(filter(lambda x : x > node.val, lst))
        
#     def convertBST(self, root):
#         """
#         :type root: TreeNode
#         :rtype: TreeNode
#         """
#         if not root: return root
#         lst = []
#         self._traverse(root, lst)
#         self._change(root, lst)
#         return root

class Solution:
    def __init__(self):
        self.total = 0
        
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        """
        Time: O(n)
        Space: O(n)
        """
        if root is not None:
            self.convertBST(root.right)
            self.total += root.val
            root.val = self.total
            self.convertBST(root.left)
        return root