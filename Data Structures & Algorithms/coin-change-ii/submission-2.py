class Solution:
    def recur(self, i, amount, coins, dp):
        if amount == 0:
            return 1
        if i == 0:
            ans = 0
            if amount % coins[0] == 0:
                ans = 1
            return ans
        if dp[i][amount] != -1:
            return dp[i][amount]
        pick = 0
        if coins[i] <= amount:
            pick = self.recur(i, amount - coins[i], coins, dp)
        
        not_pick = self.recur(i-1, amount, coins, dp)

        dp[i][amount] = pick + not_pick

        return dp[i][amount]

    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        # dp = [[-1 for _ in range(amount + 1)] for _ in range(n)]
        # return self.recur(n-1, amount, coins, dp)

        dp = [[0 for _ in range(amount + 1)] for _ in range(n+1)]
        
        dp[0][0] = 1
        for i in range(1, n+1):
            dp[i][0] = 1
            for am in range(amount+1):
                dp[i][am] = dp[i-1][am]
                if coins[i-1] <= am:
                    dp[i][am] += dp[i][am - coins[i-1]]
        
        return dp[n][amount]
        