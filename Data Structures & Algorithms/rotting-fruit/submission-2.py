class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        fresh = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))
        time = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while fresh > 0 and len(queue) > 0:
            time += 1
            q_size = len(queue)
            for i in range(q_size):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2
                    queue.append((nr, nc))
                    fresh -= 1
        
        if fresh > 0:
            return -1
        return time
