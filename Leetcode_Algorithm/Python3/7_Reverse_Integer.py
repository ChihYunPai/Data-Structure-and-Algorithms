"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output:  321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

"""

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        pos_limit = str(2**31)
        neg_limit = str(2**31 - 1)
        string = ''.join([c for c in str(abs(x))[::-1]])
        string = '0' * (len(pos_limit) - len(string)) + string
        if x < 0:
            return 0 if string > pos_limit else -int(string)
        else:
            return 0 if string > neg_limit else int(string)
