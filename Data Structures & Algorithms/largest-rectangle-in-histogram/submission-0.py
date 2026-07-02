class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        n = len(heights)
        maxArea = 0
        for i in range(n + 1):
            while stack and (i == n or heights[i] <= heights[stack[-1]]):
                idx = stack.pop()
                height = heights[idx]
                width = i
                if stack:
                    width = i - stack[-1] - 1
                maxArea = max(maxArea, height * width)
            stack.append(i)
        return maxArea
        