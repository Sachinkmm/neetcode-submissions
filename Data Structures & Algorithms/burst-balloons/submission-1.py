class Solution:
    def recur(self, l, r, nums, mp):
        # if len(nums) == 2:
        #     return 0
        if l > r:
            return 0
        if (l, r) in mp:
            return mp[(l, r)]
        maxCoins = 0
        for i in range(l, r+1):
            coins = nums[l-1] * nums[i] * nums[r+1]
            coins += self.recur(l, i-1, nums, mp) + self.recur(i+1, r, nums, mp)
            maxCoins = max(maxCoins, coins)
        mp[(l, r)] = maxCoins
        return mp[(l, r)]

    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        mp = {}
        ans = self.recur(1, n-2, nums, mp)
        return ans
        