class Solution:
    def recur(self, i, j, s, p):
        slen = len(s)
        plen = len(p)
        if j == plen:
            return i == slen
        
        same = False
        if i < slen and (p[j] == "." or s[i] == p[j]):
            same = True
        if (j + 1) < len(p) and p[j+1] == "*":
                nopick = self.recur(i, j+2, s, p)
                pick = same and self.recur(i+1, j, s, p)
                return nopick or pick
        if same:
            return self.recur(i+1, j+1, s, p)
        return False
    
    def isMatch(self, s: str, p: str) -> bool:
        return self.recur(0, 0, s, p)
        