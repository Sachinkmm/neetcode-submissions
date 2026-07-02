class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l, r= 0, n-1
        ans = 0
        while l < r:
            minHeight = min(heights[l], heights[r])
            ans = max(ans, (r - l) * minHeight)
            while l < r and heights[l] <= minHeight:
                l += 1
            while l < r and heights[r] <= minHeight:
                r -= 1
        return ans

        