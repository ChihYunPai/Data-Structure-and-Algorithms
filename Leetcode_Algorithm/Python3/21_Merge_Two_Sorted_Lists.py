"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        """
        O(n)
        loop while l1 or l2
        """
        
        lstNode = ListNode(None)
        begin = lstNode
        while l1 or l2:
            if l1 and l2:
                if l1.val <= l2.val:
                    lstNode.next = ListNode(l1.val)
                    l1 = l1.next
                else:
                    lstNode.next = ListNode(l2.val)
                    l2 = l2.next
                lstNode = lstNode.next
            elif l1:
                while l1:
                    lstNode.next = ListNode(l1.val)
                    l1 = l1.next
                    lstNode = lstNode.next
            elif l2:
                while l2:
                    lstNode.next = ListNode(l2.val)
                    l2 = l2.next
                    lstNode = lstNode.next
            else:
                pass
        return begin.next