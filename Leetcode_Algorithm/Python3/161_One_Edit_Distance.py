"""
Given two strings S and T, determine if they are both one edit distance apart.
Ex:


s =      ''   'a'   'a'   'abc'   'ab'
t =      ''   ''    'A'   'ab'    'acb'
return   F     T     T     T       T
"""
class Solution:
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s and not t: return False
        if not s or not t: return True
        ls, lt = len(s), len(t)
        
        if abs(ls - lt) > 1: return False
        
        i = j = diff = 0
        while i < ls and j < lt:
            if s[i] != t[j]:
                diff += 1
                if diff > 1: return False
                if i < ls - 1 and s[i+1] == t[j]: i += 1
                elif j < lt - 1 and s[i] == t[j+1]: j += 1
            i += 1
            j += 1
        if i < ls or j < lt: diff += 1
        if diff == 1: return True
        return False