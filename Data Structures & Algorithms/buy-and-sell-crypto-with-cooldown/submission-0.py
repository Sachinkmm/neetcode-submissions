class Solution:
    def recur(self, i, buying, prices):
        if i >= len(prices):
            return 0
        
        cooldown = self.recur(i+1, buying, prices)
        if buying:
            buy = self.recur(i+1, 0, prices) - prices[i]
            return max(cooldown, buy)
        else:
            sell = self.recur(i+2, 1, prices) + prices[i]
            return max(cooldown, sell)

    
    def maxProfit(self, prices: List[int]) -> int:
        return self.recur(0, True, prices)
        