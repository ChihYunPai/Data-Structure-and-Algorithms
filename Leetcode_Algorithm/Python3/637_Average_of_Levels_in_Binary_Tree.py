"""
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def __mean(self, lst):
        if len(lst) == 0:
            return 0
        return float(sum(lst)) / float(len(lst))
    
    def __traverse(self, root, lst, h=1):
        if not root:
            return
        lst.append((root.val, h))
        self.__traverse(root.left, lst, h+1)
        self.__traverse(root.right, lst, h+1)
        
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []
        lst = result = []
        self.__traverse(root, lst)
        heights = set(map(lambda x: x[1], lst))
        lst = [[x[0] for x in lst if x[1] == height] for height in heights]
        return list(map(lambda x: self.__mean(x), lst))