class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        pref = [0] * n
        suff = [0] * n
        pref[0] = nums[0]
        suff[-1] = nums[-1]
        for i in range(1, n):
            pref[i] = pref[i-1] * nums[i]
        for i in range(n-2, -1, -1):
            suff[i] = suff[i+1] * nums[i]
        
        ans[0] = suff[1]
        ans[-1] = pref[n-2]
        for i in range(1, n-1):
            ans[i] = pref[i-1] * suff[i+1]
        return ans
            
        