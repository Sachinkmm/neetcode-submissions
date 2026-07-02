class Solution:
    def recur(self, r, c, prev, matrix):
        if (r < 0 or c < 0 or r >= len(matrix) or c >= len(matrix[0]) or
            matrix[r][c] <= prev):
            return 0

        # UP
        up = 1 + self.recur(r - 1, c, matrix[r][c], matrix)
        # Down
        down = 1 + self.recur(r + 1, c, matrix[r][c], matrix)
        # Left
        left = 1 + self.recur(r, c - 1, matrix[r][c], matrix)
        # Right
        right = 1 + self.recur(r, c + 1, matrix[r][c], matrix)
        
        return max(up, down, left, right)

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans = max(ans, self.recur(i, j, -1, matrix))
        return ans
        