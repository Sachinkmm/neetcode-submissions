class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        sum_so_far = nums[0]
        for i in range(1, len(nums)):
            sum_so_far += nums[i]
            sum_so_far = max(sum_so_far, nums[i])
            ans = max(ans, sum_so_far)
        return ans
        