class DSU {
    private int[] parent, size;

    public DSU(int n) {
        parent = new int[n + 1];
        size = new int[n + 1];
        for (int i = 0; i <= n; i++) {
            parent[i] = i;
            size[i] = 1;
        }
    }

    public int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }

        return parent[x];
    }

    public boolean union(int u, int v) {
        int pu = find(parent[u]);
        int pv = find(parent[v]);

        if (pu == pv) {
            return false;
        }

        if (size[pu] >= size[pv]) {
            parent[pv] = pu;
            size[pu] += size[pv];
        }
        else {
            parent[pu] = pv;
            size[pv] += size[pu];
        }
        return true;
    }
}

class Solution {
    public int getIndex(int r, int c, int Cols) {
        return r * Cols + c;
    }

    public int numIslands(char[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
        int islands = 0;
        DSU dsu = new DSU(rows * cols + 1);
        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == '1') {
                    islands++;
                    for (int[] dir : directions) {
                        int nr = r + dir[0];
                        int nc = c + dir[1];
                        if (nr < 0 || nc < 0 || nr >= rows || nc >= cols || grid[nr][nc] == '0') {
                            continue;
                        }
                        if (dsu.union(getIndex(r, c, cols), getIndex(nr, nc, cols))) {
                            islands--;
                        }
                    }
                }
            }
        }
        return islands;
    }
}
