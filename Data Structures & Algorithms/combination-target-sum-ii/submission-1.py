class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        tmp = []
        candidates.sort()

        def dfs(i, target):
            if target == 0:
                ans.append(tmp.copy())
                return
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j-1] == candidates[j]:
                    continue

                if target - candidates[j] < 0:
                    break
                tmp.append(candidates[j])
                dfs(j+1, target - candidates[j])
                tmp.pop()

        dfs(0, target)
        return ans