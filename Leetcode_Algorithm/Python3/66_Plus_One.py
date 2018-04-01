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
        Time: O(n)
        Space: O(1)
        """
        # optional input validation
        assert(len(digits) > 0)
        for digit in digits:
            assert(type(digit) is int and 0 <= digit <= 9)

        # loop body
        for i in range(len(digits)-1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                break
            # else: digits[i] == 9
            digits[i] = 0

        # check the first digit
        if digits[0] == 0:
            digits.insert(0, 1)
        return digits
