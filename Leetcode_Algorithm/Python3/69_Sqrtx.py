"""
Implement int sqrt(int x).

Compute and return the square root of x.

x is guaranteed to be a non-negative integer.


Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we want to return an integer, the decimal part will be truncated.
"""

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        prev = xn = x
        while xn * xn > x:
            prev = xn
            xn = (xn + x/xn) / 2 
            if (prev - xn) < 1: break
        return int(xn//1)