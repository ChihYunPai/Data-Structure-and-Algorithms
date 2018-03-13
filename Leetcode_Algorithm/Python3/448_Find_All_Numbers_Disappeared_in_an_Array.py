"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]

"""

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
        #1: shortest
        """
        # return list(set(range(1, len(nums)+1)) - set(nums))
        """
        #2: fastest
        Time: O(n)
        Space: O(n)
        247 ms
        """
        # res = []
        # lst = [False] * len(nums)
        # for i in nums:
        #     lst[i-1] = True
        # return [i+1 for i in range(len(nums)) if not lst[i]]
        """
        #3:
        Time: O(n)
        Space: O(1)
        426 ms
        """
        res = []
        n = len(nums)
        for i in range(n):
            nums[(nums[i]-1) % n] += n
        return [i+1 for i in range(n) if nums[i] <= n]
        