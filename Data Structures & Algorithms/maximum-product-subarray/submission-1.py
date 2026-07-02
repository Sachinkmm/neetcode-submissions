class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        mini, maxi = 1, 1
        for num in nums:
            tmp = mini
            mini = min(num, mini * num, maxi * num)
            maxi = max(num, tmp * num, maxi * num)
            ans = max(ans, maxi)
        
        return ans
        