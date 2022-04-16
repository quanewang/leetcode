# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l = 0
        r = len(nums) - 1
        while l < r and nums[r] == nums[l]:
            r -= 1
        if l == r:
            return nums[r] == target

        if nums[l] > nums[r]:
            l0 = l
            r0 = r
            origin = -1
            while l0 < r0:
                m0 = (l0 + r0) / 2
                if nums[m0] < nums[l]:
                    r0 = m0 - 1
                else:
                    l0 = m0 + 1
            if nums[r0] < nums[l]:
                origin = r0
            else:
                origin = r0 + 1

            if nums[l] <= target:
                return self.bin_search(nums, target, l, origin - 1)
            else:
                return self.bin_search(nums, target, origin, r)
        else:
            return self.bin_search(nums, target, l, r)

    def bin_search(self, nums, target, l, r):
        while l < r:
            m = (l + r) / 2
            if nums[m] == target:
                return True
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        if l == r:
            return nums[l] == target
        return False

