"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

"""
import sys
class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        """
        Time: O(N^2)
        Space: O(1)
        """
        nums.sort()
        res, diff = 0, sys.maxsize
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                threeSum = nums[i] + nums[left] + nums[right]
                diff_temp = abs(threeSum - target)
                if threeSum == target:
                    return target
                if diff_temp < diff:
                    diff = diff_temp
                    res = threeSum
                if threeSum < target:
                    left += 1
                else:
                    right -= 1
        return res