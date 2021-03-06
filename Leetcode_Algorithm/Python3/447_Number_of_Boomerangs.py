"""
Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:
Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
"""
################################################################
# Old version

# class Solution:
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         counter = list(collections.Counter(s).values())
#         return sum([2*(x//2) for x in counter]) + any([x%2==1 for x in counter])

class Solution:
    
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        return sum(n*(n-1) for x1, y1 in points for n in collections.Counter((x1-x2)**2 + (y1-y2)**2 for x2, y2 in points).values())