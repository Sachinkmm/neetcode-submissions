class Solution:
    def expand_center(self, s, i, j):
        res = 0
        while i >= 0 and j < len(s) and s[i] == s[j]:
            res += 1
            i -= 1
            j += 1
        return res

    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            res += self.expand_center(s, i, i)
            res += self.expand_center(s, i, i+1)
        
        return res
        