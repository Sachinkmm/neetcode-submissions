class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        m = len(grid)
        n = len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    ans += 1
                    self.fill(i, j, grid)

        return ans
    
    def fill(self, r, c, grid):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == "0":
            return
        grid[r][c] = "0"
        self.fill(r - 1, c, grid)
        self.fill(r + 1, c, grid)
        self.fill(r, c - 1, grid)
        self.fill(r, c + 1, grid)