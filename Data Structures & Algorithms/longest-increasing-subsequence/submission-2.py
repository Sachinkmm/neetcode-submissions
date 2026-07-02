class Solution:
    def recur(self, i, j, nums):
        if i == len(nums):
            return 0
        pick = 0
        if j == -1 or nums[i] > nums[j]:
            pick = 1 + self.recur(i+1, i, nums)
        not_pick = self.recur(i+1, j, nums)

        return max(pick, not_pick)

    def lengthOfLIS(self, nums: List[int]) -> int:
        return self.recur(0, -1, nums)

        LIS = [1] * len(nums)

        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)
        