"""
Given an n-ary tree, return the preorder traversal of its nodes' values.


For example, given a 3-ary tree:




Return its preorder traversal as: [1,3,5,6,2,4].


Note: Recursive solution is trivial, could you do it iteratively?

"""
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    """
    Iteration
    """
    
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        lst = []
        if not root:
            return lst
        stack = [root]
        while len(stack) > 0:
            node = stack.pop()
            lst.append(node.val)
            for child in node.children[::-1]:
                stack.append(child)
        return lst

    """
    Recursion
    """
    #     def _preorder(self, node, lst):
    #         if node:
    #             lst.append(node.val)
    #             for child in node.children:
    #                 self._preorder(child, lst)

    #     def preorder(self, root):
    #         """
    #         :type root: Node
    #         :rtype: List[int]
    #         """
    #         lst = []
    #         if not root:
    #             return lst
    #         self._preorder(root, lst)
    #         return lst


