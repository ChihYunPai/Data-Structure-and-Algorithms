"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = ['(', '{', '[']
        right = [')', '}', ']']
        stack = []
        for c in s:
            if c in left:
                stack.append(c)
            elif c in right:
                if len(stack) == 0: return False
                if right.index(c) != left.index(stack.pop()): return False
        if len(stack) != 0: return False
        return True