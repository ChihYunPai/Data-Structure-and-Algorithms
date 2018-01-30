"""
171. Excel Sheet Column Number
DescriptionHintsSubmissionsDiscussSolution
Discuss Pick One
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
"""

class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        for i in reversed(range(len(s))):
            num += 26**(len(s)-1-i) * (ord(s[i]) - 64)
        return num