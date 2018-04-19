"""
Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.

Note:
Given target value is a floating point.
You may assume k is always valid, that is: k ≤ total nodes.
You are guaranteed to have only one unique set of k values in the BST that are closest to the target.
Follow up:
Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from queue import PriorityQueue as PQueue
class Solution:
    def traverse(self, node, pqueue, target):
        if not node: return 
        pqueue.put((abs(target - node.val), node.val))
        if node.left:
            self.traverse(node.left, pqueue, target)
        if node.right:
            self.traverse(node.right, pqueue, target)
            
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode<float>, 
        :type target: float
        :type k: int, range: [0:n]
        :rtype: List[int]
        """
        if not root: return None
        pqueue = PQueue()
        res = [0]*k
        self.traverse(root, pqueue, target)
        for i in range(k):
            _, res[i] = pqueue.get()
        return res