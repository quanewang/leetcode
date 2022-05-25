"""
https://leetcode.com/problems/partition-list/
86. Partition List
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.
Example 1:
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
Example 2:

Input: head = [2,1], x = 2
Output: [1,2]
"""


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
        l0 = l = head
        while l:
            while l and l.val < x:
                l0 = l
                l = l.next
            if l:
                r = r0 = l
                while r and r.val >= x:
                    r0 = r
                    r = r.next
                if r:
                    if l == l0:
                        head = self.swap(l0, r0)
                    else:
                        self.swap(l0, r0)
