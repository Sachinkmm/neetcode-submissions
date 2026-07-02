class Solution:
    def recur(self, i, target, nums):
        if i < 0:
            return 1 if target == 0 else 0
        
        add = self.recur(i-1, target - nums[i], nums)
        sub = self.recur(i-1, target + nums[i], nums)
        return add + sub

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        return self.recur(n-1, target, nums)
        