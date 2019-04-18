"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    Time: O(n)
    Space: O(n)
    n: max(len(l1), len(l2))
    """
    def addTwoNumbers(self, l1, l2):
        result_node = ListNode(0)
        result = result_node
        
        while l1 or l2:
            carry, digit = 0, 0
            
            if not l1:
                digit = l2.val
                l2 = l2.next
            elif not l2:
                digit = l1.val
                l1 = l1.next
            else:
                sum_ = l1.val + l2.val
                carry, digit = (sum_ // 10), (sum_ % 10)
                l1, l2 = l1.next, l2.next
                
            result_node.val += digit
            carry, result_node.val = (carry + result_node.val // 10), (result_node.val % 10)
            
            if l1 or l2 or carry:
                result_node.next = ListNode(carry)
                result_node = result_node.next
                
        return result
    
            
#         """
#         First method:
#         """
#         #===================================
#         # decode l1 to num1         O(n)
#         # decode l2 to num2         O(n)
#         # total = num1 + num2       O(1)
#         # encode total to result    O(n)
#         # return result             O(1)
#         #===================================
#         #                           O(3n)
#         #===================================
# #         count = num1 = 0
# #         while l1:
# #             num1 += (l1.val * (10 ** count))
# #             count += 1
# #             l1 = l1.next
            
# #         count = num2 = 0
# #         while l2:
# #             num2 += (l2.val * (10 ** count))
# #             count += 1
# #             l2 = l2.next
            
# #         lst = [y for y in str(num1 + num2)[::-1]]
# #         result = ListNode(lst[0])
# #         curr = result
# #         for x in lst[1:]:
# #             curr.next = ListNode(x)
# #             curr = curr.next
# #         return result
    
#         """
#         Second method:
#         """
#         #===================================
#         # carry = 0
#         # while l1 or l2 not end     O(n)
#         #     num = curr1 + curr2 + carry
#         # .   carry = num // 10
#         #     
#         #     lst.append(num % 10)
#         # if carry:
#         #     lst.append(carry)
                
#         #===================================
#         #                              O(n)
#         #===================================
# #         notStart = False
# #         result = None
# #         carry = 0
# #         while l1 or l2 or carry:
# #             if l1 and l2: 
# #                 num = l1.val + l2.val + carry
# #                 l1 = l1.next
# #                 l2 = l2.next
# #             elif l1:
# #                 num = l1.val + carry
# #                 l1 = l1.next
# #             elif l2:
# #                 num = l2.val + carry
# #                 l2 = l2.next
# #             else: num = carry
                
# #             if notStart:
# #                 curr.next = ListNode(num % 10)
# #                 curr = curr.next
# #             else:
# #                 result = ListNode(num % 10)
# #                 curr = result
# #                 notStart = True
# #             carry = num // 10
# #         return result