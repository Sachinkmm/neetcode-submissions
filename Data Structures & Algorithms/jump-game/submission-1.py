class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[0] = True
        for i in range(n):
            if dp[i] == False:
                return False
            if nums[i] + i >= n:
                return True
            for j in range(1, nums[i] + 1):
                dp[i+j] = True
            # print(dp)
        return dp[n-1]