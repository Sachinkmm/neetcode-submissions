class Solution:
    def recur(self, i, prev, nums):
        if i == len(nums):
            return 0
        pick = 0
        if nums[i] > prev:
            pick = 1 + self.recur(i+1, nums[i], nums)
        not_pick = self.recur(i+1, prev, nums)

        return max(pick, not_pick)

    def lengthOfLIS(self, nums: List[int]) -> int:
        return self.recur(0, -1000, nums)
        