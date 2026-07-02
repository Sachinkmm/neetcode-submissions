class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = []
        q = []
        for i in range(n):
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            if i + 1 >= k:
                ans.append(nums[q[0]])
            while q and q[0] <= (i - k + 1):
                q.pop(0)
        return ans
            
        