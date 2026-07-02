class Solution:
    def recur(self, i, j, s, p, mp):
        slen = len(s)
        plen = len(p)
        if j == plen:
            return i == slen
        
        if (i, j) in mp:
            return mp[(i, j)]
        
        same = False
        if i < slen and (p[j] == "." or s[i] == p[j]):
            same = True
        if (j + 1) < len(p) and p[j+1] == "*":
                nopick = self.recur(i, j+2, s, p, mp)
                pick = same and self.recur(i+1, j, s, p, mp)
                mp[(i, j)] = nopick or pick
                return mp[(i, j)]
        if same:
            mp[(i, j)] = self.recur(i+1, j+1, s, p, mp)
            return mp[(i, j)]
        return False
    
    def isMatch(self, s: str, p: str) -> bool:
        mp = {}
        return self.recur(0, 0, s, p, mp)
        