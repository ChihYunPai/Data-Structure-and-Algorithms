"""
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def __inorderTraverse(self, root, lst=[]):
        if root==None: return
        self.__inorderTraverse(root.left, lst)
        lst.append(root.val)
        self.__inorderTraverse(root.right, lst)
        
    
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root==None: return []
        lst = []
        self.__inorderTraverse(root, lst)
        return lst