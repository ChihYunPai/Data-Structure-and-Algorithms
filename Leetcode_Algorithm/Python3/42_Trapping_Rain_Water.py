"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!
"""

"""
Time O(n)
Space: O(1)
"""
class Solution:
    def trap(self, height):
        """
        :type height: List[int], int >= 0
        :rtype: int
        """
        # input validation
        if len(height) < 3:
            return 0
        assert(len(height) >= 0 and all([isinstance(x, int) for x in height]))

        # initialization
        water, l, l_max, r, r_max = 0, 0, 0, len(height) - 1, 0

        # process
        while l < r:
            l_max = max(l_max, height[l])
            r_max = max(r_max, height[r])
            if height[l] < height[r]:
                l += 1
                water += max(0, (min(l_max, r_max) - height[l]))
            else: # height[l] >= height[r]
                r -= 1
                water += max(0, (min(l_max, r_max) - height[r]))
        return water


"""
Time: O(n^2), Time Limit Exceeded
Space: O(n)
"""
# from copy import deepcopy
# from collections import defaultdict
# class Solution:
#     def trap(self, height):
#         """
#         :type height: List[int], int >= 0
#         :rtype: int
#         """

#         # input validation
#         if len(height) < 3:
#             return 0
#         assert(len(height) > 0 and all([isinstance(x, int) for x in height]))
        
#         # initialization
#         lw = set()
#         rw = set()
#         water = 0
#         acc = defaultdict(int)
        
#         # process
#         prevHeight = 0
#         for i, currHeight in enumerate(height):
#             if prevHeight < currHeight: # goes up
#                 rw |= (lw & set([x for x in range(prevHeight + 1, currHeight + 1)]))
                
#             elif prevHeight > currHeight: # goes down
#                 lw |= set([x for x in range(currHeight + 1, prevHeight + 1)])
                
#             else: # prevHeight == currHeight
#                 pass
            
#             intersection = copy.deepcopy(lw & rw)
#             # print('==============')
#             # print(prevHeight, currHeight)
#             # print('lw: ', lw)
#             # print('rw: ', rw)
#             # print('intersection: ', intersection)
#             # print('acc: ', acc)
#             for wall in intersection:
#                 water += acc[wall]
#                 acc[wall] = 0
#                 # print(wall)
#                 # print('lw: ', lw)
#                 # print('rw: ', rw)
#                 rw.remove(wall)
#                 lw.remove(wall)
                
#             if len(lw):
#                 for h in lw:
#                     acc[h] += 1
            
            
#             prevHeight = currHeight
                
#         return water