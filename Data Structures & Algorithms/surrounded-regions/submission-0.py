class Solution:
    def dfs(self, r, c, dp):
        if (r < 0 or c < 0 or r >= len(dp) or c >= len(dp[0])
            or dp[r][c] in ["X", "#"]):
            return
        
        dp[r][c] = "#"
        dirc = [(-1, 0),(1, 0),(0, -1),(0, 1)]
        for dr, dc in dirc:
            nr, nc = dr + r, dc + c
            self.dfs(nr, nc, dp)
    
    def solve(self, board: List[List[str]]) -> None:
        dp = board.copy()
        m = len(board)
        n = len(board[0])

        for i in range(m):
            self.dfs(i, 0, dp)
            self.dfs(i, n-1, dp)
        
        for j in range(n):
            self.dfs(0, j, dp)
            self.dfs(m-1, j, dp)
        
        # print(dp)
        
        for i in range(m):
            for j in range(n):
                if dp[i][j] == "O":
                    board[i][j] = "X"
                elif dp[i][j] == "#":
                    board[i][j] = "O"
        return
        