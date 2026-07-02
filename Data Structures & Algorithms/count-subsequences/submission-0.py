class Solution:
    def recur(self, i, j, s, t, tmp):
        if j < 0:
            return 1
        if i < 0:
            return 0
        
        npick = self.recur(i-1, j, s, t, tmp)
        if s[i] == t[j]:
            npick += self.recur(i-1, j-1, s, t, tmp)
        
        return npick

    def numDistinct(self, s: str, t: str) -> int:
        s_len = len(s)
        t_len = len(t)
        return self.recur(s_len-1, t_len-1, s, t, "")
        