class Solution:
    def expand_center(self, s, i, j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return s[i+1:j]
    
    def manacher(self, s):
        t = '#' + '#'.join(s) + '#'
        n = len(t)
        p = [0] * n
        c, r = 0, 0

        for i in range(n):
            mirror = 2 * c - i # Mirror of i with respect to center c
            if i < r:
                p[i] = min(r - i, p[mirror]) # Use the mirrored palindrome's value if possible
            
            # Expand around center i
            while (i + p[i] + 1 < n and i - p[i] - 1 >= 0 and
                t[i + p[i] + 1] == t[i - p[i] - 1]):
                p[i] += 1
            
            if i + p[i] > r:
                c = i
                r = i + p[i]
        return p

    def longestPalindrome(self, s: str) -> str:
        # ans = ""
        # for i in range(len(s)):
        #     tmp1 = self.expand_center(s, i, i)
        #     tmp2 = self.expand_center(s, i, i+1)
        #     if len(tmp1) > len(ans):
        #         ans = tmp1
        #     if len(tmp2) > len(ans):
        #         ans = tmp2
        # return ans
        p = self.manacher(s)
        resLen, center_idx =  max((v, i) for i, v in enumerate(p)) 
        resIdx = (center_idx - resLen) // 2

        return s[resIdx:resIdx+resLen]     