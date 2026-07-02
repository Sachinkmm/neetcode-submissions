class Solution:
    def recur(self, i, target, nums, dp):
        if i < 0:
            return 1 if target == 0 else 0
        if (i, target) in dp:
            return dp[(i, target)]
        add = self.recur(i-1, target - nums[i], nums, dp)
        sub = self.recur(i-1, target + nums[i], nums, dp)
        dp[(i, target)] = add + sub
        return dp[(i, target)]

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # dp = [[-1] * (target + 1) for _ in range(n)]
        dp = {}
        return self.recur(n-1, target, nums, dp)
        