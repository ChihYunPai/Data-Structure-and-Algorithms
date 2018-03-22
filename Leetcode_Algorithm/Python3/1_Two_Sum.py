"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
class Solution:
    import collections
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        Time: O(nlogn)
        Space: O(n)
        """
        # numsSort = sorted(nums)
        # keys = sorted(range(len(nums)), key=lambda x: nums[x])
        # low, high = 0, len(nums)-1
        # while (numsSort[low] + numsSort[high]) != target:
        #     print(low, high)
        #     if (numsSort[low] + numsSort[high]) < target:
        #         low += 1
        #     else:
        #         high -= 1
        # return [keys[low], keys[high]]
        

        """
        Time: O(n)
        Space: O(n)
        """
        dic = collections.defaultdict(list)
        for i, num in enumerate(nums):
            dic[num].append(i)
            
        for i, num in enumerate(nums):
            if (target - num) == num:
                if len(dic[(target - num)]) == 2:
                    return [min(dic[(target - num)]), max(dic[(target - num)])]
            elif len(dic[(target - num)]) == 1:
                return sorted([dic[target - num][0], dic[num][0]])

        
            