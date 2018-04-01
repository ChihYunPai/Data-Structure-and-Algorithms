"""
Given an n-ary tree, return the postorder traversal of its nodes' values.


For example, given a 3-ary tree:




Return its postorder traversal as: [5,6,3,2,4,1].


Note: Recursive solution is trivial, could you do it iteratively?
"""
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
"""
Recursion
"""
# class Solution(object):
#     def _postorder(self, node, lst):
#         if node:
#             for child in node.children:
#                 self._postorder(child, lst)
#             lst.append(node.val)
        
#     def postorder(self, root):
#         """
#         :type root: Node
#         :rtype: List[int]
#         """
#         lst = []
#         if not root:
#             return lst
#         self._postorder(root, lst)
#         return lst
"""
Iteration
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        lst = []
        if not root:
            return lst
        stack = [root]
        dic = {}
        while len(stack):
            node = stack[-1]
            for child in node.children[::-1]:
                if child not in lst:
                    stack.append(child)
            if node == stack[-1]: # all children of the node are in lst already 
                node = stack.pop()
                lst.append(node.val)
            
        return lst

