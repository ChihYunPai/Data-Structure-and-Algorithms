"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
"""

class Solution:
    
    def traverse(self, root, lst=[], subList=[]):
        if root==None:
            return []
        if subList==[]:
            subList = [root.val]
        if root.left==None and root.right==None:
            lst.append(subList)
            return
        if root.left:
            self.traverse(root.left, lst, subList + [root.left.val])
        if root.right:
            self.traverse(root.right, lst, subList + [root.right.val])
    
    def pathSum(self, root, sum_int):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        lst = []
        if root==None:
            return lst
        
        # traverse and return all possible paths in List[List[int]]
        self.traverse(root, lst)
        
        # choose those List[int] in all possible paths List[List[int]] that fits the sum(List[int]) == sum
        return [x for x in lst if sum(x)==sum_int] # easier to read than filter()