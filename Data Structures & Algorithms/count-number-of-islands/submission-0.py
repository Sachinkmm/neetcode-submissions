class Solution:
    def dfs(self, r, c, grid):
        if (r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or
            grid[r][c] == "-1" or grid[r][c] == "0"):
            return
        grid[r][c] = "-1"
        # UP
        self.dfs(r - 1, c, grid)
        # DOWN
        self.dfs(r + 1, c, grid)
        # LEFT
        self.dfs(r, c - 1, grid)
        # RIGHT
        self.dfs(r, c + 1, grid)
        
    def numIslands(self, grid: List[List[str]]) -> int:
        self.ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.ans += 1
                    self.dfs(i, j, grid)
        # print(grid)
        return self.ans