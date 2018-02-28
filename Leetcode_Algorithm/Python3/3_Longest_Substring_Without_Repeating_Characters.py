"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""

class Solution:
    
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        Time: O(n)
        Space: O(1)
        """
        index = maxLength = 0
        for (i, c) in enumerate(s):
            if c in s[index:i]:
                maxLength = max(maxLength, i - index)
                index += s[index:i].index(c) + 1
        return max(maxLength, len(s[index:]))