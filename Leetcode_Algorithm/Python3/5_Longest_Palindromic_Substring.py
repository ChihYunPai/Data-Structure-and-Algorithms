"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
 

Example:

Input: "cbbd"

Output: "bb"

"""

# class Solution:
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         """
#         First method: O(n^2)
#         """
#         if s == s[::-1]: return s
#         for k in range(len(s)-1, 0, -1):
#             for i in range(0, len(s) - k + 1):
#                 substring = s[i:i+k]
#                 if substring == substring[::-1]:
#                     return s[i:i+k]
