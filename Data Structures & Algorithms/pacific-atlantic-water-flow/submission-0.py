class Solution:
    def dfs(self, r, c, visit, heights, prev):
        if ((r, c) in visit or r < 0 or r >= len(heights) or c < 0 or c >= len(heights[0])
            or heights[r][c] < prev):
            return
        
        visit.add((r, c))
        self.dfs(r - 1, c, visit, heights, heights[r][c])
        self.dfs(r + 1, c, visit, heights, heights[r][c])
        self.dfs(r, c - 1, visit, heights, heights[r][c])
        self.dfs(r, c + 1, visit, heights, heights[r][c])

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        pac = set()
        atl = set()

        for i in range(m):
            self.dfs(i, 0, pac, heights, heights[i][0]) #pacific
            self.dfs(i, n-1, atl, heights, heights[i][n-1]) #atlantic
        
        for j in range(n):
            self.dfs(0, j, pac, heights, heights[0][j]) #pacific
            self.dfs(m-1, j, atl, heights, heights[m-1][j]) #atlantic
        
        ans = []
        for i in range(m):
            for j in range(n):
                if (i, j) in pac and (i, j) in atl:
                    ans.append([i, j])
        
        return ans
        