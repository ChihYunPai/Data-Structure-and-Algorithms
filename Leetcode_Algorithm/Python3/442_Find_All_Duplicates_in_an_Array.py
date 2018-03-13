"""
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
        Time: O(n)
        Space: O(n)
        571 ms
        """
        # counter = collections.Counter(nums)
        # return [x for x in counter.keys() if counter[x] == 2]
        
        """
        Time: O(n)
        Space: O(1)
        260 ms
        """
        # res = []
        # n = len(nums)
        # lst = [0] * n
        # for i in range(n):
        #     lst[nums[i] - 1] += 1
        # return [i+1 for i in range(n) if lst[i] == 2]

        """
        Time: O(n)
        Space: O(1)
        373 ms
        """
        # res = []
        # n = len(nums)
        # for i in range(n):
        #     nums[(nums[i]-1) % n] += n
        # for i in range(n):
        #     if nums[i] > (2 * n):
        #         res.append(i+1)
        # return res

        """
        Time: O(n)
        Space: O(1)
        297 ms
        """
        res = []
        for x in nums:
            if nums[abs(x)-1] < 0:
                res.append(abs(x))
            else:
                nums[abs(x)-1] *= -1
        return res