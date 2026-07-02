class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        store = set(nums)

        for num in nums:
            streak = 0
            curr = num
            while curr in store:
                curr += 1
                streak += 1
            ans = max(ans, streak)
        return ans
        