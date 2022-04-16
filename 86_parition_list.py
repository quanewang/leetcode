# Definition for singly-linked list.
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        head0 = tail0 = None
        head1 = tail1 = None

        while head:
            if head.val < x:
                head0, tail0 = self.append(head0, tail0, head)
            else:
                head1, tail1 = self.append(head1, tail1, head)
            tmp = head.next
            head.next = None
            head = tmp
        if tail0:
            tail0.next = head1
        if head0:
            return head0
        else:
            return head1

    def append(self, head, tail, node):
        if not head:
            head = tail = node
        else:
            tail.next = node
            tail = node
        return head, tail
