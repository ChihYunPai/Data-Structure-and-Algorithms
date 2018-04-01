"""
Given a string, find the length of the longest substring T that contains at most k distinct characters.

For example, Given s = “eceba” and k = 2,

T is "ece" which its length is 3.
"""

from collections import defaultdict
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: unicode, 0 <= len(s)
        :type k: int, 0 <= k
        :rtype: int
        """
        # input validation
        if len(s) == 0 or k == 0:
            return 0
        if k >= len(s):
            return len(s)
        
        # initialization
        max_length, left = 0, 0
        dic = defaultdict(list)
        
        # process 
        for i, char in enumerate(s):
            dic[char] = i
            if len(dic) > k: # violates rule
                # delete the left most character
                left = min(dic.values())
                del dic[s[left]]
                left += 1
            max_length = max(max_length, i - left + 1)
        return max_length
