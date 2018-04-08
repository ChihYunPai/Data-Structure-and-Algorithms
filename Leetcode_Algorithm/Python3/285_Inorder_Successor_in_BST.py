"""
Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

Note: If the given node has no in-order successor in the tree, return null.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from Queue import LifoQueue as Stack

"""
Time: O(log n)
Space: O(1)
"""
class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        successor = None
        while root:
            if p.val < root.val:
                successor, root = root, root.left
            else:
                root = root.right
        return successor

"""
Time: O(n)
Space: O(n)
"""
class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        # input validation
        assert(isinstance(root, TreeNode) and isinstance(p, TreeNode))
        if root == None:
            return None
        
        # inorderTraversal
        stack = Stack()
        current = root
        found = False
        while True:
            if current != None:
                stack.put(current)
                current = current.left
            else:
                if not stack.empty():
                    current = stack.get()
                    if current == p and found == False:
                        found = True
                    elif current != p and found == True:
                        return current
                    current = current.right
                else:
                    break