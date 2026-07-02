class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    self.fill(i, j, grid, 0)
    
    def fill(self, r, c, grid, dis):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == -1 or dis > grid[r][c]:
            return
        
        grid[r][c] = min(grid[r][c], dis)
        self.fill(r - 1, c, grid, dis + 1)
        self.fill(r + 1, c, grid, dis + 1)
        self.fill(r, c - 1, grid, dis + 1)
        self.fill(r, c + 1, grid, dis + 1)