class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        tmp = []

        def backtrack(i):
            res.append(tmp.copy())
            # if i == len(nums):
            #     res.append(tmp.copy())
            #     return
            
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue
                tmp.append(nums[j])
                backtrack(j + 1)
                tmp.pop()
            # tmp.append(nums[i])
            # backtrack(i+1)
            # tmp.pop()

            # while i + 1 < len(nums) and nums[i] == nums[i+1]:
            #     i += 1
            # backtrack(i+1)
        
        backtrack(0)
        return res
        