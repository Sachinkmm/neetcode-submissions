class Solution:
    def recur(self, i, op, s, dp):
        if op < 0:
            return False
        if i >= len(s):
            return op == 0
        
        if dp[i][op] != -1:
            return dp[i][op]
        res = False
        if s[i] == '(':
            res = self.recur(i+1, op + 1, s, dp)
        elif s[i] == ')':
            res = self.recur(i+1, op - 1, s, dp)
        else:
            if self.recur(i+1, op, s, dp):
                res = True
            if not res and self.recur(i+1, op + 1, s, dp):
                res = True
            if not res and self.recur(i+1, op - 1, s, dp):
                res = True
        dp[i][op] = res
        return res

    def checkValidString(self, s: str) -> bool:
        n = len(s)
        dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]
        return self.recur(0, 0, s, dp)
        