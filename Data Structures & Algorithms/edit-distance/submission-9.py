class Solution:

    def recur(self, i, j, w1, w2, dp):
        if i < 0:
            return j + 1
        if j < 0:
            return i + 1
        
        if dp[i][j] != -1:
            return dp[i][j]

        ans = float('inf')
        if w1[i] == w2[j]:
            ans = self.recur(i-1, j-1, w1, w2, dp)
        else:
            insert = self.recur(i, j-1, w1, w2, dp)
            dele = self.recur(i-1, j, w1, w2, dp)
            rep = self.recur(i-1, j-1, w1, w2, dp)
            ans = 1 + min(insert, dele, rep)
        
        dp[i][j] = ans
        return dp[i][j]

    def minDistance(self, word1: str, word2: str) -> int:
        lw1 = len(word1)
        lw2 = len(word2)

        dp = [[-1 for _ in range(lw2 + 1)] for _ in range(lw1 + 1)]

        return self.recur(lw1 - 1, lw2 - 1, word1, word2, dp)