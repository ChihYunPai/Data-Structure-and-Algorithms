"""
In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Example 1:
Input: 
nums = 
[[1,2],
 [3,4]]
r = 1, c = 4
Output: 
[[1,2,3,4]]
Explanation:
The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.
Example 2:
Input: 
nums = 
[[1,2],
 [3,4]]
r = 2, c = 4
Output: 
[[1,2],
 [3,4]]
Explanation:
There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.
Note:
The height and width of the given matrix is in range [1, 100].
The given r and c are all positive.
"""
# class Solution:
#     def matrixReshape(self, nums, r, c):
#         """
#         :type nums: List[List[int]]
#         :type r: int
#         :type c: int
#         :rtype: List[List[int]]
#         """
#         if sum([len(x) for x in nums]) != (r*c):
#             return nums
#         #rearrange nums to vector
#         vector = []
#         for i in range(0, len(nums)):
#             for j in range(0, len(nums[0])):
#                 vector.append(nums[i][j])
#                 print(nums[i][j])
#         #rearrange vector to matrix
#         reshapeMatrix = []
#         print(r, c, vector)
#         for i in range(0, r):
#             row = []
#             for j in range(0, c):
#                 row.append(vector.pop(0))
#             reshapeMatrix.append(row)
#         return reshapeMatrix

class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if sum([len(x) for x in nums]) != (r*c):
            return nums
        reshapeMatrix = [[0 for i in range(0,c)] for j in range(0,r)]
        #rearrange nums to reshapeMatrix
        for index in range(0, r*c):
            reshapeMatrix[index//c][index%c] = nums[index//len(nums[0])][index%len(nums[0])]
        return reshapeMatrix

# inpt = [[1,2],[3,4]]
# r, c = 4, 1
# sol = Solution
# print(sol.matrixReshape(sol, inpt, r, c))
