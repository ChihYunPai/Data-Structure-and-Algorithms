"""
Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

For example, given nums = [3, 5, 2, 1, 6, 4], one possible answer is [1, 6, 2, 5, 3, 4].
"""

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        sortedNums = sorted(nums)
        i, j = 0, 0
        while i < len(nums):
            nums[i] = sortedNums[j]
            i += 2
            j += 1
        i = len(nums) - 1 if len(nums) % 2 == 0 else len(nums) - 2
        while i >= 1:
            nums[i] = sortedNums[j]
            i -= 2
            j += 1
        