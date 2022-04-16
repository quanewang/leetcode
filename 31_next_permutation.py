# https://leetcode.com/problems/next-permutation/

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        while i:
            j = i - 1
            while j >= 0:
                if nums[i] > nums[j]:
                    return self.mutate(nums, i, j)
                j -= 1
            i -= 1
        nums.sort()
        return nums

    def mutate(self, nums, i, j):
        tmp = nums[j]
        nums[j] = nums[i]
        nums[i] = tmp
        tail = nums[j + 1:]
        tail.sort()
        return nums[0:j + 1] + tail

s = Solution()

print(s.nextPermutation([1,3,2]))