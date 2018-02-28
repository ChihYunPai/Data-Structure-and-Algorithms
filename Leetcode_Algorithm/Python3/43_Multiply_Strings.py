"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.

Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""
class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # return str(int(num1) * int(num2))
        
        length = len(num1) + len(num2)
        carry = 0
        lst = []
        
        if len(num1) > len(num2):
            num2 = '0' * (len(num1) - len(num2)) + num2
        elif len(num2) > len(num1):
            num1 = '0' * (len(num2) - len(num1)) + num1
        
        num = 0
        for i, n1 in enumerate(num1[::-1]):
            for j, n2 in enumerate(num2[::-1]):
                num += int(n1) * int(n2) * (10**(i+j))
        return str(num)