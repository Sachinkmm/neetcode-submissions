class Solution:
    def rob(self, nums: List[int]) -> int:
        # n = len(nums)
        # if n < 2:
        #     return nums[0]
        # nums[1] = max(nums[0], nums[1])
        # for i in range(2, n):
        #     nums[i] = max(nums[i-1], nums[i-2] + nums[i])
        # return max(nums[n-1], nums[n-2])
        rob1, rob2 = 0, 0

        for num in nums:
            temp = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
        