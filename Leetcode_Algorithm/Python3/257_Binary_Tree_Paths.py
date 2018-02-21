"""
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def traverse(self, lst, root, string):
        if(root.left==None and root.right==None):
            lst.append(string)
            return 
        if(root.left): 
            self.traverse(lst, root.left, string + "->" + str(root.left.val))
        if(root.right): 
            self.traverse(lst, root.right, string + "->" + str(root.right.val))
    
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        lst = []
        if(root == None): return lst
        self.traverse(lst, root, str(root.val))
        return lst


###################################################################################################
# another concise solution:

# class Solution:
    
#     def binaryTreePaths(self, root, lst=[], string=""):
#         """
#         :type root: TreeNode
#         :rtype: List[str]
#         """
#         if not root:
#             return []
#         return [str(root.val) + "->" + path
#                for child in (root.left, root.right) if child
#                for path in self.binaryTreePaths(child)] or [str(root.val)]
