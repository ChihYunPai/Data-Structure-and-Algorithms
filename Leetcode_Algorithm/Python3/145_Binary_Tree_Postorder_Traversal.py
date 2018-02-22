"""
Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],

   1
    \
     2
    /
   3
 

return [3,2,1].

Note: Recursive solution is trivial, could you do it iteratively?

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def __postorderTraversal(self, root=None, lst=[]):
        if root==None: return
        self.__postorderTraversal(root.left, lst)
        self.__postorderTraversal(root.right, lst)
        lst.append(root.val)
    
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root==None: return []
        lst = []
        self.__postorderTraversal(root, lst)
        return lst
        
        