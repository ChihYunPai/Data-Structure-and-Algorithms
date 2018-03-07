"""
Reverse a singly linked list.

Hint:
A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    
    def recursive(self, prev, head):
        if head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        else: return prev
        return self.recursive(prev, head)
        
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        """
        Iterative
        """
        # prev = None
        # while head:
        #     next = head.next
        #     head.next = prev
        #     prev = head
        #     head = next
        # return prev
        """
        Recursive
        """
        prev = None
        return self.recursive(prev, head)