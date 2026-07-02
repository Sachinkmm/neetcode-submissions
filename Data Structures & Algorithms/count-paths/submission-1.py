class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev = [1] * n
        curr = [1] * n

        for i in range(1, m):
            for j in range(1, n):
                curr[j] += curr[j-1]
        
        return curr[n-1]
        