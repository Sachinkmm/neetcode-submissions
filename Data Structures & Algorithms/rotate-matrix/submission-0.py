class Solution:
    def transpose(self, matrix):
        for i in range(self.n):
            for j in range(i+1, self.n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def swapOnMid(self, matrix):
        for i in range(self.n):
            for j in range(self.n // 2):
                matrix[i][j], matrix[i][self.n-1-j] = matrix[i][self.n-1-j], matrix[i][j]

    def rotate(self, matrix: List[List[int]]) -> None:
        self.n = len(matrix)
        self.transpose(matrix)
        self.swapOnMid(matrix)

