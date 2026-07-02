class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen = set()
            for j in range(9):
                if board[row][j] == '.':
                    continue
                if board[row][j] in seen:
                    return False
                seen.add(board[row][j])

        for col in range(9):
            seen = set()
            for i in range(9):
                if board[i][col] == '.':
                    continue
                if board[i][col] in seen:
                    return False
                seen.add(board[i][col])
        
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == '.':
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True