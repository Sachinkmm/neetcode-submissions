class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        sum_so_far = 0
        for num in nums:
            sum_so_far += num
            sum_so_far = max(sum_so_far, num)
            ans = max(ans, sum_so_far)
        return ans
        