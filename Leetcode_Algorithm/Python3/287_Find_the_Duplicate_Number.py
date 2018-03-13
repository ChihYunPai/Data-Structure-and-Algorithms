"""
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
"""
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        Time: O(n^2)
        Space: O(1)
        """
        # for x in set(nums):
        #     if nums.count(x) > 1:
        #         return x
        
        """
        Time: O(n)
        Space: O(n)
        """
        # counter = collections.Counter(nums)
        # return [x for x in counter.keys() if counter[x] > 1][0]

        """
        Time: O(n)
        Space: O(1)
        """
        finder = fast = slow = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        while True:
            slow = nums[slow]
            finder = nums[finder]
            if slow == finder:
                return finder