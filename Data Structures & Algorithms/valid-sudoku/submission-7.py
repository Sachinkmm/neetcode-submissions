class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        sq = [0] * 9

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                val  = int(board[r][c]) - 1
                if (1 << val) & rows[r]:
                    return False
                if (1 << val) & cols[c]:
                    return False
                if (1 << val) & sq[(r//3)*3 + (c//3)]:
                    return False
                rows[r] |= (1 << val)
                cols[c] |= (1 << val)
                sq[(r//3)*3 + (c//3)] |= (1<<val)
        return True 
    '''
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # return self.helper(0, 0, board)
        from collections import defaultdict
        rows, cols, boxes = defaultdict(set), defaultdict(set), defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    boxes[(i//3, j//3)].add(board[i][j])
        def solve(r, c):
            if r == 9:
                return True
            if c == 9:
                return solve(r+1, 0)
            
            if board[r][c] == ".":
                for i in range(1, 10):
                    i = str(i)
                    if i not in rows[r] and i not in cols[c] and i not in boxes[(r//3,c//3)]:
                        rows[r].add(i)
                        cols[c].add(i)
                        boxes[(r//3,c//3)].add(i)
                        board[r][c] = i

                        if solve(r, c+1):
                            return True
                        board[r][c] = "."
                        rows[r].remove(i)
                        cols[c].remove(i)
                        boxes[(r//3,c//3)].remove(i)
            else:
                return solve(r, c+1)
            return False
        return solve(0, 0)
    
    def helper(self, row, col, board):
        if row == 9:
            return True
        if col == 9:
            return self.helper(row+1, 0, board)
        if board[row][col] == ".":
            for k in range(1, 10):
                if self.checkValid(row, col, str(k), board):
                    board[row][col] = str(k)
                    if self.helper(row, col+1, board):
                        return True
                    board[row][col] = "."
            return False
        else:
            return self.helper(row, col+1, board)
    
    def checkValid(self, r, c, ch, board):
        for i in range(9):

            if board[i][c] == ch:
                return False
            if board[r][i] == ch:
                return False
            if board[3*(r//3)+i//3][3*(c//3)+i%3] == ch:
                return False
        return True
    
    def isValid(self, r, c, ch, board):
        return self.rowValid(r, c, ch, board) and self.colValid(r, c, ch, board) and self.isBoxValid(r, c, ch, board)
    
    def rowValid(self, r, c, ch, board):
        for j in range(len(board[0])):
            if j != c and board[r][j] == ch:
                return False
        return True
    
    def colValid(self, r, c, ch, board):
        for i in range(len(board)):
            if i != r and board[i][c] == ch:
                return False
        return True
    
    def isBoxValid(self, r, c, ch, board):
        m = r // 3
        n = c // 3
        for i in range(m*3, m*3 + 3):
            for j in range(n*3, n*3 + 3):
                if i == r and j == c:
                    continue
                if board[i][j] == ch:
                    return False
        return True
    '''