class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        dp = board.copy()

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or dp[r][c] in ["X", "#"]:
                return
            dp[r][c] = "#"
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc)

        for row in range(rows):
            dfs(row, 0)
            dfs(row, cols - 1)
        
        for col in range(cols):
            dfs(0, col)
            dfs(rows - 1, col)
        
        for i in range(rows):
            for j in range(cols):
                if dp[i][j] == "#":
                    board[i][j] = "O"
                elif dp[i][j] == "O":
                    board[i][j] = "X"
        return