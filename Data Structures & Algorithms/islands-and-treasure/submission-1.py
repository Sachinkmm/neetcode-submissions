class Solution:
    def dfs(self, r, c, grid, dis):
        if (r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or
            grid[r][c] == -1 or grid[r][c] < dis):
            return
        
        grid[r][c] = min(grid[r][c], dis)
        # UP
        self.dfs(r - 1, c, grid, dis + 1)
        # DOWN
        self.dfs(r + 1, c, grid, dis + 1)
        # LEFT
        self.dfs(r, c - 1, grid, dis + 1)
        # RIGHT
        self.dfs(r, c + 1, grid, dis + 1)

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    self.dfs(i, j, grid, 0)
        return
        