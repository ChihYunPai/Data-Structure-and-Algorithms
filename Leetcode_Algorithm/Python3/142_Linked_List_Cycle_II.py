"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        """
        #1
        """
        # if not head or not head.next: return None
        # slow = fast = head
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        #     if slow is fast: break
        # if not fast or not fast.next: return None
        # fast = head
        # while fast is not slow:
        #     slow = slow.next
        #     fast = fast.next
        # return fast
        """
        #2
        """
        isCycle = False
        try:
            slow = fast = head
            while slow and fast:
                slow = slow.next
                fast = fast.next.next
                if slow == fast: 
                    isCycle = True
                    break
        except:
            pass
        if not isCycle: return None
        fast = head
        while fast is not slow:
            slow = slow.next
            fast = fast.next
        return fast