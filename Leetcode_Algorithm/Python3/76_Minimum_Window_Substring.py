"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.

"""
from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t: return ""
        if len(t) > len(s): return ""
        count = Counter(t)
        dic = defaultdict(list)
        full = False
        res = None
        best = float('inf')
        minimal = []
        toVisit = set(count.keys())
        
        for i, char in enumerate(s):
            if char not in count:
                continue
            dic[char].append(i)
            minimal.append(i)
            if len(dic[char]) == count[char]:
                if char in toVisit: 
                    toVisit.remove(char)
            elif len(dic[char]) > count[char]:
                if char in toVisit: 
                    toVisit.remove(char)
                minimal.remove(dic[char].pop(0))
            if not full:
                if not toVisit:
                    full = True
            if full:
                dist = i - minimal[0]
                if dist < best:
                    best = dist
                    res = [minimal[0], i]
        if not res: return ""
        return s[res[0]:res[1]+1]