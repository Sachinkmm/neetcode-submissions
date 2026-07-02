class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # BFS
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        count = 1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] != 2147483647:
                        continue
                    grid[nr][nc] = count
                    q.append((nr, nc))
            count += 1


        ''' DFS
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    self.fill(i, j, grid, 0)
        '''
    
    def fill(self, r, c, grid, dis):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == -1 or dis > grid[r][c]:
            return
        
        grid[r][c] = min(grid[r][c], dis)
        self.fill(r - 1, c, grid, dis + 1)
        self.fill(r + 1, c, grid, dis + 1)
        self.fill(r, c - 1, grid, dis + 1)
        self.fill(r, c + 1, grid, dis + 1)