"""
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
"""
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        high = low = maxProd = nums[0]
        for num in nums[1:]:
            high, low = max(num, high * num, low * num), min(num, high * num, low * num)
            maxProd = max(a, high)
        return maxProd
            