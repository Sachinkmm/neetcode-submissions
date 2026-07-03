class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        pac, alt = set(), set()

        def dfs(r, c, visit, hgt):
            if (r, c) in visit or r < 0 or r >= m or c < 0 or c >= n or heights[r][c] < hgt:
                return
            
            visit.add((r, c))
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])

        for col in range(n):
            dfs(0, col, pac, heights[0][col]) # pac
            dfs(m-1, col, alt, heights[m-1][col]) # atl
        
        for row in range(m):
            dfs(row, 0, pac, heights[row][0]) # pac
            dfs(row, n-1, alt, heights[row][n-1]) # alt
        ans = []
        for i in range(m):
            for j in range(n):
                if (i, j) in pac and (i, j) in alt:
                    ans.append([i, j])
        
        return ans