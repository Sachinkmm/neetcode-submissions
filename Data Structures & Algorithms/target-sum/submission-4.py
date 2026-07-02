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
        # dp = {}
        # return self.recur(n-1, target, nums, dp)
        dp = [defaultdict(int) for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(n):
            for total, count in dp[i].items():
                dp[i+1][total + nums[i]] += count
                dp[i+1][total - nums[i]] += count
        
        return dp[n][target]
        