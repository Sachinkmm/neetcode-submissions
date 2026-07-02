class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            ind = abs(nums[i]) - 1
            if nums[ind] < 0:
                return ind+1
            nums[ind] = -1 * nums[ind]
        
        