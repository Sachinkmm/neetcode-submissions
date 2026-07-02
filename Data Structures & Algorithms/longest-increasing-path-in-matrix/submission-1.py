class Solution:
    def recur(self, r, c, prev, matrix, dp):
        if (r < 0 or c < 0 or r >= len(matrix) or c >= len(matrix[0]) or
            matrix[r][c] <= prev):
            return 0
        if (r, c) in dp:
            return dp[(r,c)]
        # UP
        up = 1 + self.recur(r - 1, c, matrix[r][c], matrix, dp)
        # Down
        down = 1 + self.recur(r + 1, c, matrix[r][c], matrix, dp)
        # Left
        left = 1 + self.recur(r, c - 1, matrix[r][c], matrix, dp)
        # Right
        right = 1 + self.recur(r, c + 1, matrix[r][c], matrix, dp)
        dp[(r,c)] = max(up, down, left, right)
        return dp[(r,c)]

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ans = 0
        dp = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans = max(ans, self.recur(i, j, -1, matrix, dp))
        return ans
        