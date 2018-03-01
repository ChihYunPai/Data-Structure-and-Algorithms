"""
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.

"""
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int], 0 <= int, len(digits) > 0
        :rtype: List[int]
        """
        """
        First version
        """
#         carry = 0
#         for i in range(len(digits)-1, -1, -1):
#             num = digits[i] + 1 if i==(len(digits)-1) else digits[i] + carry
#             carry = num // 10
#             digits[i] = num % 10
#         if carry != 0:
#             digits.insert(0, carry)
#         return digits

        """
        Better one
        """
    
        for i in range(len(digits)-1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                break
            digits[i] = 0
        if digits[0] == 0:
            digits.insert(0, 1)
        return digits
            
        