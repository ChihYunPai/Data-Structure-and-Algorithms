"""
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
"""
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        """
        N: length of height list
        Time: O(N)
        Space: O(1)
        """
        # assert(len(height) > 0)
        # assert(all([x >= 0 for x in height]))
        maxArea, i, j = 0, 0, len(height) - 1
        while i < j:
            maxArea = max(maxArea, min(height[i], height[j]) * (j - i))
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return maxArea