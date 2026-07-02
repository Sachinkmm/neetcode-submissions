class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        miss = n
        for i in range(n):
            miss ^= i
            miss ^= nums[i]
        return miss
        