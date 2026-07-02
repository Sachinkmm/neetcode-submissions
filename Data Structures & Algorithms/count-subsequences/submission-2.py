class Solution:
    def recur(self, i, j, s, t, dp):
        if j < 0:
            return 1
        if i < 0:
            return 0
        
        if dp[i][j] != -1:
            return dp[i][j]
        dp[i][j] = self.recur(i-1, j, s, t, dp)
        if s[i] == t[j]:
            dp[i][j] += self.recur(i-1, j-1, s, t, dp)
        
        return dp[i][j]

    def numDistinct(self, s: str, t: str) -> int:
        s_len = len(s)
        t_len = len(t)
        # dp = [[-1 for _ in range(t_len + 1)] for _ in range(s_len + 1)]
        # return self.recur(s_len-1, t_len-1, s, t, dp)

        dp = [[0 for _ in range(t_len + 1)] for _ in range(s_len + 1)]
        
        for i in range(s_len+1):
            dp[i][0] = 1
        for i in range(1, s_len+1):
            for j in range(1, t_len+1):
                dp[i][j] = dp[i-1][j]
                if s[i-1] == t[j-1]:
                    dp[i][j] += dp[i-1][j-1]
        
        return dp[s_len][t_len]