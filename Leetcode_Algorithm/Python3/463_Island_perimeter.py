"""
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
Explanation: The perimeter is the 16 yellow stripes in the image below:
...
"""

# class Solution:
#     def islandPerimeter(self, grid):
#         """
#         :type grid: List[List[int]]
#         :rtype: int
#         """
#         width, height = len(grid[0]), len(grid)
#         totalEdges = 0
#         heightEdge = [0, height-1]
#         widthEdge = [0, width-1]
            
#         for i in range(height):
#             for j in range(width):
#                 if height==1 and grid[i][j]==1:
#                     totalEdges += 2
#                 elif i in heightEdge and grid[i][j]==1:
#                     totalEdges += 1
                    
#                 if width==1 and grid[i][j]==1:
#                     totalEdges += 2
#                 elif j in widthEdge and grid[i][j]==1:
#                     totalEdges += 1
                    
#                 if j != 0 and grid[i][j] != grid[i][j-1]:
#                     totalEdges += 1
#                 if i != 0 and grid[i][j] != grid[i-1][j]:
#                     totalEdges += 1
#         return totalEdges


class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        width, height, totalEdges = len(grid[0]), len(grid), 0
            
        for i in range(height):
            for j in range(width):
                if grid[i][j]==1:
                    totalEdges += 4
                    if i>0 and grid[i-1][j]==1:
                        totalEdges -= 2
                    if j>0 and grid[i][j-1]==1:
                        totalEdges -= 2
        return totalEdges