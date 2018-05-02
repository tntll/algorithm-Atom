# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single
# digit. Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except
# the number 0 itself.
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans = sums = ListNode(-1)
        carry = 0
        while l1 and l2:
            sums.next = ListNode(l1.val + l2.val + carry)
            carry = sums.next.val//10
            sums.next.val %= 10
            sums = sums.next
            l1 = l1.next
            l2 = l2.next
        res = l1 or l2
        while res:
            sums.next = ListNode(res.val + carry)
            carry = sums.next.val//10
            sums.next.val %= 10
            sums = sums.next
            res = res.next
        if carry:
            sums.next = ListNode(1)
        return ans.next


class Solution2:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans = sums = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            carry, val = divmod(carry, 10)
            sums.next = ListNode(val)
            sums = sums.next
        return ans.next
