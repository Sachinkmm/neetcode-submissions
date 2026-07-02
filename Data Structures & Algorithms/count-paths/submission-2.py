class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # curr = [1] * n

        # for i in range(1, m):
        #     for j in range(1, n):
        #         curr[j] += curr[j-1]
        
        # return curr[n-1]
        if m == 1 or n == 1:
            return 1
        
        if m < n:
            return self.uniquePaths(n, m)
        
        res = j = 1
        for i in range(m, m + n - 1):
            res *= i
            res //= j
            j += 1
        return res
        