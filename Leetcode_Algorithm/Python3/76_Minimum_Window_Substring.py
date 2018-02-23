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
################################################################
# Time Limit Exceeded 
################################################################
class Solution:
    import collections
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        B = collections.Counter(t)
        for k in range(len(t), len(s)+1):
            for i in range(len(s) - k + 1):
                A = collections.Counter(s[i:i+k])
                if B.keys() == A.keys() & B.keys(): # all in 
                    if all([B[x] <= A[x] for x in B.keys()]): # counts all less and equal
                        return s[i:i+k]
        return ""

        