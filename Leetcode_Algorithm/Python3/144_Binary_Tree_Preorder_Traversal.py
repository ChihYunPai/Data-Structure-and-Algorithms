"""
Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3
return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

################################################################
# FIRST VERSION
class Solution:
    def __preorderTraverse(self, root, lst):
        if root==None: return
        lst.append(root.val)
        self.__preorderTraverse(root.left, lst)
        self.__preorderTraverse(root.right, lst)
        
    def preorderTraversal(self, root, lst=[]):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root==None: return []
        lst = []
        self.__preorderTraverse(root, lst)
        return lst