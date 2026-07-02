class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        row, col = 0, 0
        ans = []
        while row < m and col < n:
            for j in range(col, n):
                ans.append(matrix[row][j])
            row += 1

            for i in range(row, m):
                ans.append(matrix[i][n-1])
            n -= 1

            if row < m:
                for j in range(n-1, col - 1, -1):
                    ans.append(matrix[m-1][j])
            m -= 1

            if col < n:
                for i in range(m-1, row - 1, -1):
                    ans.append(matrix[i][col])
            col += 1
        return ans


        