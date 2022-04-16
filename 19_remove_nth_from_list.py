# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p = head
        count = n - 1
        while p and count:
            p = p.next
            count -= 1
        if count or not p:
            return head
        q = head
        q0 = None
        while p.next:
            q0 = q
            q = q.next
            p = p.next
        if q0:
            q0.next = q.next
        else:
            head = q.next
        return head

