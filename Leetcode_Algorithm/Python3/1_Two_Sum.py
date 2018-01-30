"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numsSort = sorted(nums)
        keys = sorted(range(len(nums)), key=lambda x: nums[x])
        low, high = 0, len(nums)-1
        while (numsSort[low] + numsSort[high]) != target:
            print(low, high)
            if (numsSort[low] + numsSort[high]) < target:
                low += 1
            else:
                high -= 1
        return [keys[low], keys[high]]