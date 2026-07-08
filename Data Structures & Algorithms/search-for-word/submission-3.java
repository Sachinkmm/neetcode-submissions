class Solution {
    public boolean exist(char[][] board, String word) {
        for (int r = 0; r < board.length; r++) {
            for (int c = 0; c < board[0].length; c++) {
                if (dfs(r, c, 0, board, word)) {
                    return true;
                }
            }
        }
        return false;
    }

    public boolean dfs(int r, int c, int idx, char[][] board, String word) {
        if (idx == word.length()) {
            return true;
        }
        if (r < 0 || c < 0 || r >= board.length || c >= board[0].length || board[r][c] != word.charAt(idx)) {
            return false;
        }
        board[r][c] = '#';

        if (dfs(r - 1, c, idx + 1, board, word)) return true;
        if (dfs(r + 1, c, idx + 1, board, word)) return true;
        if (dfs(r, c - 1, idx + 1, board, word)) return true;
        if (dfs(r, c + 1, idx + 1, board, word)) return true;

        board[r][c] = word.charAt(idx);
        return false;
    }
}
