"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".
"""

class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        """
        First version
        """
#         vowels = "aeiouAEIOU"
#         if s == "": return ""
#         sList = list(s)
#         stack = [x for x in s if x in vowels]
#         for i, c in enumerate(sList):
#             if c not in vowels: continue
#             sList[i] = stack.pop()
#         return ''.join(sList)
        
        
        """
        Second version
        """
        vowels = "aeiouAEIOU"
        if len(s) <= 1:
            return s
        sList = list(s)
        i, j = 0, len(sList)-1
        while i < j:
            if sList[i] not in vowels:
                i += 1
                continue
            if sList[j] not in vowels:
                j -= 1
                continue
            sList[i], sList[j] = sList[j], sList[i]
            i += 1
            j -= 1
        return ''.join(sList)