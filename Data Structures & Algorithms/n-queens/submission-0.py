class Solution:
    def isSafe(self, r, c, board):
        row = r - 1
        while row >= 0:
            if board[row][c] == "Q":
                return False
            row -= 1
        
        row, col = r-1, c-1
        while row >= 0 and col >= 0:
            if board[row][col] == "Q":
                return False
            row, col = row - 1, col - 1
        
        row, col = r-1, c+1
        while row >= 0 and col < len(board):
            if board[row][col] == "Q":
                return False
            row, col = row - 1, col + 1
        
        return True

    def solveNQueens(self, n: int) -> List[List[str]]:
        queen = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                tmp = ["".join(row) for row in board]
                queen.append(tmp)
                return
            
            for c in range(n):
                if self.isSafe(r, c, board):
                    board[r][c] = "Q"
                    backtrack(r+1)
                    board[r][c] = "."
        
        backtrack(0)
        return queen
        