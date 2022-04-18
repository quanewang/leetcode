# https://leetcode.com/problems/jump-game-ii/

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        q = [(0, 0)]
        cache = set()
        while q:
            i, count = q.pop(0)
            if i==len(nums)-1:
                return count
            elif i<len(nums)-1 and ((i + nums[i])>=len(nums)-1):
                return count+1
            elif i<len(nums)-1:
                for j in range(i+1, i+nums[i]+1):
                    if nums[j] and j not in cache:
                        q.append((j, count+1))
                        cache.add(j)
        return 0
s = Solution()
print(s.jump([8,2,4,4,4,9,5,2,5,8,8,0,8,6,9,1,1,6,3,5,1,2,6,6,0,4,8,6,0,3,2,8,7,6,5,1,7,0,3,4,8,3,5,9,0,4,0,1,0,5,9,2,0,7,0,2,1,0,8,2,5,1,2,3,9,7,4,7,0,0,1,8,5,6,7,5,1,9,9,3,5,0,7,5]))