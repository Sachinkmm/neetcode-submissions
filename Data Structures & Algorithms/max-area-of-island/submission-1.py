class Solution:
    def dfs(self, r, c, grid):
        if (r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0])
            or grid[r][c] == 0):
            return 0
        
        grid[r][c] = 0
        # UP
        up = self.dfs(r - 1, c, grid)
        # DOWN
        down = self.dfs(r + 1, c, grid)
        # LEFT
        left = self.dfs(r, c - 1, grid)
        # RIGHT
        right = self.dfs(r, c + 1, grid)

        return 1 + up + down + left + right

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    ans = max(ans, self.dfs(i, j, grid))
        
        return ans