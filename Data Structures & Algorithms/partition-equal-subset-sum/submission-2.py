class Solution:
    def recur(self, i, target, nums, dp):
        if i < 0:
            return False
        if target == 0:
            return True
        
        if dp[i][target] != -1:
            return dp[i][target]

        pick = False
        if nums[i] <= target:
            pick = self.recur(i - 1, target - nums[i], nums, dp)
        not_pick = self.recur(i - 1, target, nums, dp)
        dp[i][target] = pick or not_pick
        return dp[i][target]

    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2:
            return False
        target = total_sum // 2
        # dp = [[-1] * (target + 1) for _ in range(len(nums))]
        # return self.recur(len(nums)-1, target, nums, dp)

        dp = [False] * (target + 1)

        dp[0] = True
        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]


        return dp[target]
        