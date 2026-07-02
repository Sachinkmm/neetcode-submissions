class Solution:
    def recur(self, i, amount, coins, dp):
        if amount == 0:
            return 0
        if i < 0:
            return float('inf')
        if i == 0:
            if amount == 0 or amount % coins[i] == 0:
                return amount // coins[i]
            else:
                return float('inf')
        
        if dp[i][amount] != -1:
            return dp[i][amount]

        pick = float('inf')
        if coins[i] <= amount:
            pick = 1 + self.recur(i, amount - coins[i], coins, dp)
        not_pick = self.recur(i-1, amount, coins, dp)

        dp[i][amount] = min(pick, not_pick)
        return dp[i][amount]

    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[-1] * (amount + 1) for _ in range(n)]
        total_coins = self.recur(len(coins)-1, amount, coins, dp)
        return -1 if total_coins == float('inf') else total_coins
        