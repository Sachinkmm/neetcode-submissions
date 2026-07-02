class Solution:
    def expand_center(self, s, i, j):
        res = 0
        while i >= 0 and j < len(s) and s[i] == s[j]:
            res += 1
            i -= 1
            j += 1
        return res
    
    def manacher(self, s):
        t = '#' + '#'.join(s) + '#'
        n = len(t)
        p = [0] * n
        c, r = 0, 0

        for i in range(n):
            mirror = 2 * c - i
            if i < r:
                p[i] = min(r - i, p[mirror])
            
            while (i + p[i] + 1 < n and i - p[i] - 1 >= 0 and
                t[i + p[i] + 1] == t[i - p[i] - 1]):
                p[i] += 1
            
            if i + p[i] > r:
                c = i
                r = i + p[i]
            
        return p
            

    def countSubstrings(self, s: str) -> int:
        res = 0

        # for i in range(len(s)):
        #     res += self.expand_center(s, i, i)
        #     res += self.expand_center(s, i, i+1)
        
        # return res

        p = self.manacher(s)

        # resLen, center_idx = max((i, v) for v, i in enumerate(p))
        # resIdx = (center_idx - resLen) // 2

        for i in p:
            res += (i + 1) // 2
        
        return res
        