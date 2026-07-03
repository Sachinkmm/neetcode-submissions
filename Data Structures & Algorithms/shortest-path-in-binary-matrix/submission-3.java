class Solution {
    public int shortestPathBinaryMatrix(int[][] grid) {
        int n = grid.length;
        if (grid[0][0] == 1 || grid[n-1][n-1] == 1) {
            return -1;
        }

        int[][] dirs = {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};
        Queue<int[]> q = new LinkedList<>();
        boolean[][] visit = new boolean[n][n];
        visit[0][0] = true;
        q.offer(new int[]{0, 0, 1});

        while (!q.isEmpty()) {
            int[] curr = q.poll();
            int r = curr[0], c = curr[1], length = curr[2];
            if (r == n-1 && c == n-1) {
                return length;
            }
            for (int[] dir : dirs) {
                int nr = r + dir[0];
                int nc = c + dir[1];

                if (nr >= 0 && nr < n && nc >= 0 && nc < n && grid[nr][nc] == 0 && !visit[nr][nc]) {
                    visit[nr][nc] = true;
                    q.offer(new int[]{nr, nc, length + 1});
                }
            }
        }
        return -1;
    }
}