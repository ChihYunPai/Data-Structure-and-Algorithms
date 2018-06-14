"""Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

"""
First version
"""
# import copy
# class Node:
#     def __init__(self):
#         self.str = ""
#         self.lefts = 0
#         self.rights = 0
        
#     def __len__(self):
#         return len(self.str)
    
#     def add(self, x):
#         self.str += x
#         if x == "(":
#             self.lefts += 1
#         elif x == ")":
#             self.rights += 1

# def traverse(node, lst, n):
#     if len(node) == (2*n):
#         lst.append(node.str)
#         return
    
#     if node.lefts < n:
#         newNode = copy.deepcopy(node)
#         newNode.add("(")
#         traverse(newNode, lst, n)
        
#     if node.lefts > node.rights:
#         newNode = copy.deepcopy(node)
#         newNode.add(")")
#         traverse(newNode, lst, n)
    
        
# class Solution:
#     def generateParenthesis(self, n):
#         """
#         :type n: int
#         :rtype: List[str]
#         """
#         if n == 0: return []
#         if n == 1: return ["()"]
#         lst = []
#         node = Node()
#         node.add("(")
#         traverse(node, lst, n)
#         return lst

"""
Second version
"""
class Solution:
    def traverse(self, left, right, string, lst):
        if left == right == 0:
            lst.append(string)
            return

        if left > 0:
            self.traverse(left - 1, right, string + "(", lst)

        if left < right:
            self.traverse(left, right - 1, string + ")", lst)
            
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0: return []
        if n == 1: return ["()"]
        left = right = n
        lst = []
        self.traverse(left - 1, right, "(", lst)
        return lst