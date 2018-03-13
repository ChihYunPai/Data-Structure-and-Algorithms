"""
Given an array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

"""
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        #1
        """
        # counter = collections.Counter(nums)
        # return [x for x in counter.keys() if counter[x] == 1][0]
        """
        #2
        """
        return (3*sum(set(nums)) - sum(nums)) / 2