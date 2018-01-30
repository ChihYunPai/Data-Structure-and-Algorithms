"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:
[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.

"""
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        print(grid)
        height, width = len(grid), len(grid[0])
        islandFlag = 1
        for i in range(height):
            for j in range(width):
                if grid[i][j]==1:
                	
                    if i>0 and grid[i-1][j]!=0:
                        grid[i][j] = grid[i-1][j]
                    if j>0 and grid[i][j-1]!=0:
                        grid[i][j] = grid[i][j-1]
                        

                    if i<(height-1) and grid[i+1][j]!=0:
                        print('hit me')
                        grid[i+1][j] = grid[i][j]
                    if j<(width-1) and grid[i][j+1]!=0:
                        grid[i][j+1] = grid[i][j]
                        
                    if grid[i][j]==1:
                        islandFlag += 1
                        grid[i][j] = islandFlag
                    
                    print(i, j, grid)
        print(grid)
        flatList = [item for sublist in grid for item in sublist]
        flatList = list(filter(lambda a: a!=0, flatList))
        values = []
        for i in set(flatList):
            print(i, flatList.count(i))
            values.append(flatList.count(i))
        print(values)
        if len(values)==0:
            return 0
        return max(values)

grid = [[0,1],[1,1]]
island = Solution()
print(island.maxAreaOfIsland(grid))
