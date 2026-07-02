class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i in range(len(nums)):
            if target - nums[i] in mp:
                id1 = mp[target - nums[i]]
                return [id1, i]
            mp[nums[i]] = i