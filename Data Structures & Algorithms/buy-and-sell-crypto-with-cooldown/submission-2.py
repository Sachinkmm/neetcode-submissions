class Solution:
    def recur(self, i, buying, prices, dp):
        if i >= len(prices):
            return 0
        if dp[i][buying] != -1:
            return dp[i][buying]
        cooldown = self.recur(i+1, buying, prices, dp)
        if buying:
            buy = self.recur(i+1, 0, prices, dp) - prices[i]
            dp[i][buying] = max(cooldown, buy)
        else:
            sell = self.recur(i+2, 1, prices, dp) + prices[i]
            dp[i][buying] = max(cooldown, sell)
        return dp[i][buying]
    
    def maxProfit(self, prices: List[int]) -> int:
        # dp = [[-1, -1] for _ in range(len(prices)+1)]
        # return self.recur(0, True, prices, dp)
        n = len(prices)
        dp = [[0] * 2 for _ in range(n+1)]

        for i in range(n-1, -1, -1):
            for buying in [True, False]:
                if buying:
                    buy = dp[i+1][False] - prices[i] if i + 1 < n else -prices[i]
                    cooldown = dp[i+1][True] if i + 1 < n else 0
                    dp[i][1] = max(buy, cooldown)
                else:
                    sell = dp[i+2][True] + prices[i] if i + 1 < n else prices[i]
                    cooldown = dp[i+1][False] if i + 1 < n else 0
                    dp[i][0] = max(sell, cooldown)
        return dp[0][1]