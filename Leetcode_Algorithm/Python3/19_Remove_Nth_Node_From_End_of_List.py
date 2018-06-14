"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        """
        sol1:
        Time: O(N), N: length of llst
        Space: O(N), lst storing pointers of nodes
        """
        length = 0
        lst = []
        llst = head
        if n == 1 and llst.next == None:
            return []
        while True:
            lst.append(llst)
            length += 1
            if llst.next == None:
                break
            llst = llst.next
        if n == 1:
            lst[-2].next = None
        elif n == length:
            return lst[1]
        else:
            lst[-n-1].next = lst[-n+1]
        return head

        """
        sol2
        Time: O(N)
        Space: O(1)
        """
        beforeHead = ListNode(0)
        beforeHead.next = head
        p1 = p2 = beforeHead
        for i in range(n):
            p1 = p1.next
        while p1.next:
            p1 = p1.next
            p2 = p2.next
        p2.next = p2.next.next
        return beforeHead.next