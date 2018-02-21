"""
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumUp(self, root=None, sum_int=0, previous=0):
        if root==None:
            return 0
        current = previous + root.val
        return int(current==sum_int) + self.sumUp(root.left, sum_int, current) + self.sumUp(root.right, sum_int, current)
    
    def pathSum(self, root=None, sum_int=0):
        """
        :type root: TreeNode<int>, nodes: [0, 1,000], int range: [-1,000,000, +1,000,000]
        :type sum: int, range: [-int_max, +int_max]
        :rtype: int, range: [-int_max, +int_max]
        :traversal rule: must go downwards (traveling only from parent nodes to childe nodes).
        """
        if root==None:
            return 0
        return self.sumUp(root, sum_int) + self.pathSum(root.left, sum_int) + self.pathSum(root.right, sum_int)