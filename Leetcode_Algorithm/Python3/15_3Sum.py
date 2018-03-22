"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
class Solution:
    import collections
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        """
        Time: O(n^2)
        Space: O(n)
        """
        # nums.sort()
        # lst = []
        # for left in range(len(nums) - 2):
        #     if left > 0 and nums[left] == nums[left - 1]:
        #         continue
        #     middle, right = left + 1, len(nums) - 1
        #     a = nums[left]
        #     while middle < right:
        #         b = nums[middle]
        #         c = nums[right]
        #         total = a + b + c
        #         if total < 0:
        #             middle += 1
        #         elif total > 0:
        #             right -= 1
        #         else: # total < 0
        #             lst.append([a, b, c])
        #             while middle < right and nums[middle] == nums[middle + 1]:
        #                 middle += 1
        #             while middle < right and nums[right] == nums[right - 1]:
        #                 right -= 1
        #             middle += 1
        #             right -= 1
        # return lst
        """
        Time: O(n^2)
        Space: O(n)
        """
        dic={}
        for num in nums:
            if num in dic:
                dic[num]+=1
            else:
                dic[num]=1
        if 0 in dic and dic[0]>=3:
            ans=[[0,0,0]]
        else:
            ans=[]
        for n in sorted([x for x in dic if x<0], reverse=True):
            for nn in sorted([x for x in dic if x>=0]):
                chk = -(nn + n)
                if chk in dic:
                    if chk in [n,nn] and dic[chk] > 1:
                        ans.append([n, chk, nn])
                    elif chk<n: 
                        ans.append([chk, n, nn])
                    elif nn<chk:
                        ans.append([n,nn,chk])
        return ans
                        
            
        