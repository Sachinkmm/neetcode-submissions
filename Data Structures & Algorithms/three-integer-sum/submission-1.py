class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        target = 0
        ans = []
        for i in range(n):
            if i != 0 and nums[i-1] == nums[i]:
                continue
            l, r = i + 1, n-1
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    # while l < r and nums[r-1] == nums[r]:
                    #     r -= 1
        return ans
            
        