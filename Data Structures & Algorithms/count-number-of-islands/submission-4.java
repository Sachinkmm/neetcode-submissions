class Solution {
    public int numIslands(char[][] grid) {
        int res = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == '1') {
                    res += 1;
                    fill(i, j, grid);
                }
            }
        }
        return res;
    }

    public void fill(int r, int c, char[][] grid) {
        if (r < 0 || r >= grid.length || c < 0 || c >= grid[0].length || grid[r][c] == '0') {
            return;
        }

        grid[r][c] = '0';
        fill(r-1, c, grid);
        fill(r+1, c, grid);
        fill(r, c-1, grid);
        fill(r, c+1, grid);
    }
}
