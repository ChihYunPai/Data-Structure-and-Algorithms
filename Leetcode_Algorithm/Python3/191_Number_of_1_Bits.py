"""
Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.

"""
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        method 1
        """
        # return sum(list(map(int, list(bin(n)[2:]))))
        
        """
        method 2
        """
        count = 0
        while n:
            if n % 2:
                count += 1
            # or n /= 2
            n >> 1
        return count

