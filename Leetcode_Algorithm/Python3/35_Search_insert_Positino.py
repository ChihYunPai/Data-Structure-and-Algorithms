"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0

"""
import unittest
# class Solution:
#     """
#     Time: O(N)
#     Space: O(1)
#     """
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         for idx, num in enumerate(nums):
#             if target <= num:
#                 return idx
#         return len(nums)

class Solution:
    """
    Time: O(N log N)
    Space: O(1)
    """
    def searchInsert(self, nums, target):
        left, right, idx = 0, len(nums) - 1, len(nums) // 2

        while left != right and idx != left:
            if target == nums[idx]:
                return idx
            elif target < nums[idx]:
                right = idx
            else: # target > nums[idx]
                left = idx

            idx = left + (right - left) // 2

        if target < nums[left]:
            return 0 if idx == 0 else idx - 1
        elif target > nums[right]:
            return right + 1
        elif target > nums[left]:
            return left + 1
        else:
            return idx

class TestSearchInsert(unittest.TestCase):

    def test_answer(self):
        solution = Solution()

        self.assertEqual(solution.searchInsert([1,3,5,6], 2), 1)
        self.assertEqual(solution.searchInsert([1,3,5,6], 7), 4)


if __name__ == '__main__':
    unittest.main()