class Solution:
    def recur(self, i, target, nums):
        if i < 0:
            return False
        if target == 0:
            return True

        pick = False
        if nums[i] <= target:
            pick = self.recur(i - 1, target - nums[i], nums)
        not_pick = self.recur(i - 1, target, nums)
        return pick or not_pick

    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2:
            return False
        target = total_sum // 2
        return self.recur(len(nums)-1, target, nums)
        