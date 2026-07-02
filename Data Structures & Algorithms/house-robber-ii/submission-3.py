class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        rob1, rob2 = 0, 0
        for i in range(n-1):
            temp = max(rob1 + nums[i], rob2)
            rob1 = rob2
            rob2 = temp
        zero = rob2
        rob1, rob2 = 0, 0
        for i in range(1, n):
            temp = max(rob1 + nums[i], rob2)
            rob1 = rob2
            rob2 = temp
        return max(nums[0], zero, rob2)
        