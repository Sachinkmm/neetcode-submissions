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
        dp = [[-1, -1] for _ in range(len(prices)+1)]
        return self.recur(0, True, prices, dp)
        