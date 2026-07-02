class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        mapp = {}
        for num in nums:
            if num in mapp:
                return True
            mapp[num] = True
        return False