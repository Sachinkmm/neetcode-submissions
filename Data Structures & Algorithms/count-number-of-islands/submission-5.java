class Solution {
    public int numIslands(char[][] grid) {
        int rows = grid.length, cols = grid[0].length;
        int islands = 0;

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == '1') {
                    bfs(i, j, grid);
                    islands++;
                }
            }
        }
        return islands;
    }

    public void bfs(int r, int c, char[][] grid) {
        Queue<int[]> q = new ArrayDeque<>();
        grid[r][c] = '0';
        q.add(new int[]{r, c});
        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

        while (!q.isEmpty()) {
            int[] node = q.poll();
            int row = node[0], col = node[1];
            for (int[] dir : directions) {
                int nr = row + dir[0], nc = col + dir[1];
                if (nr >= 0 && nc >= 0 && nr < grid.length && nc < grid[0].length && grid[nr][nc] == '1') {
                    q.offer(new int[]{nr, nc});
                    grid[nr][nc] = '0';
                }
            }
        }
    }
}
