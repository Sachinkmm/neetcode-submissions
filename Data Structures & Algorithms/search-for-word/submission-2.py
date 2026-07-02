class Solution:
    def backtrack(self, r, c, board, i, word):
        if i == len(word):
            return True
        if r < 0 or r == len(board) or c < 0 or c == len(board[0]):
            return False
        if board[r][c] != word[i]:
            return False
        
        board[r][c] = '#'
        # visited[r][c] = 1
        # UP
        if self.backtrack(r-1, c, board, i+1, word):
            return True
        # Down
        if self.backtrack(r+1, c, board, i+1, word):
            return True
        # Left
        if self.backtrack(r, c-1, board, i+1, word):
            return True
        # Right
        if self.backtrack(r, c+1, board, i+1, word):
            return True
        # visited[r][c] = 0
        board[r][c] = word[i]

    def exist(self, board: List[List[str]], word: str) -> bool:
        # visited = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.backtrack(i, j, board, 0, word):
                    return True
        return False
        