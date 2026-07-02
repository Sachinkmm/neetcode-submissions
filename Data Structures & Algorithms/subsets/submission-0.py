import copy
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        tmp = []
        def dfs(i):
            if i >= len(nums):
                ans.append(tmp.copy())
                return
            tmp.append(nums[i])
            dfs(i+1)
            tmp.pop()
            dfs(i+1)
        
        dfs(0)
        return ans
        