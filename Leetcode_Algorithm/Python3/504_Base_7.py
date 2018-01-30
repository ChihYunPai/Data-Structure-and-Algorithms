"""
Given an integer, return its base 7 string representation.

Example 1:
Input: 100
Output: "202"
Example 2:
Input: -7
Output: "-10"
Note: The input will be in range of [-1e7, 1e7].
"""
class Solution:
    """
    Recursive Solution
    """
    def convertToBase(self, num, base):
        if num < 0:
            return '-' + self.convertToBase(-num, base)
        if num < base:
            return str(num)
        return self.convertToBase(num//base, base) + str(num%base)
    
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        """
        Direct Solution
        """
        return if num<0 '-' + str(int(str(-num, 7)) else str(int(str(num, 7))
        """
        Recursive Solution
        """
        # return self.convertToBase(num, 7)
        """
        Iterative Solution
        """

        