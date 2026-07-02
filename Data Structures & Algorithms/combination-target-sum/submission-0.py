class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        tmp = []
        
        def dfs(i, target):
            if target == 0:
                ans.append(tmp.copy())
                return
            if i == len(nums):
                return
            
            if nums[i] <= target:
                tmp.append(nums[i])
                dfs(i, target - nums[i])
                tmp.pop()
            dfs(i+1, target)
        dfs(0, target)
        
        return ans
        