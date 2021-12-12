"""
4. Median of Two Sorted Arrays
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
Example 3:

Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000
Example 4:

Input: nums1 = [], nums2 = [1]
Output: 1.00000
Example 5:

Input: nums1 = [2], nums2 = []
Output: 2.00000
"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):

        n1 = (len(nums1) + len(nums2)) // 2
        if (len(nums1) + len(nums2)) % 2 ==0:
            r1 = self.findMedianSortedArraysHelper(nums1, nums2, 0, len(nums1)-1, 0, len(nums2)-1, n1)
            n2 = n1 - 1
            r2 = self.findMedianSortedArraysHelper(nums1, nums2, 0, len(nums1)-1, 0, len(nums2)-1, n2)
            return (r1+r2)/2
        else:
            return self.findMedianSortedArraysHelper(nums1, nums2, 0, len(nums1)-1, 0, len(nums2), n1)

    def findMedianSortedArraysHelper(self, nums1, nums2, l1, r1, l2, r2, n):
        if r1<0 or r1<l1:
            return nums2[l2 + n]
        elif r2<0 or r2<l2:
            return nums1[l1 + n]

        m1 = (l1+r1)//2
        m2l, m2r = self.search(nums2, l2, r2, nums1[m1])
        if m1-l1 + m2r -l2 + 1 == n:
            return nums1[m1]
        elif m1-l1 + m2r -l2 + 1 < n:
            return self.findMedianSortedArraysHelper(nums1, nums2, m1 + 1, r1, m2r + 1, r2,
                                                     n - (m1 - l1 + m2r - l2 + 2))
        else:
            return self.findMedianSortedArraysHelper(nums1, nums2, l1, m1 - 1, l2, m2r, n)

    # modified binary search
    # r points to the element smaller than k
    # l points to the element k, or, if k does not exists, the element larger than k
    def search(self, nums, l, r, k):
        while l<=r:
            m = (l+r)//2
            if nums[m]==k:
                l = m
                r = m-1
            elif nums[m]>k:
                r = m - 1
            else:
                l = m + 1
        if l==r:
            if nums[r]>k:
                r -= 1
        return l, r

s = Solution()
print(s.findMedianSortedArrays([1,3], [2, 4]))
print(s.findMedianSortedArrays([1,3, 5, 7, 9], [2, 4, 6, 8, 10]))