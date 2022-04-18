# https://leetcode.com/problems/3sum-closest/
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        result = None
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] == target:
                    return target
                else:
                    result = self.compare(result, nums[i] + nums[l] + nums[r], target)
                    if nums[i] + nums[l] + nums[r] < target:
                        l += 1
                    else:
                        r -= 1
        return result

    def compare(self, result, attempt, target):
        if result is not None and abs(result - target) < abs(attempt - target):
            return result
        return attempt

