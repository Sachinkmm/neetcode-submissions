class Solution:
    def expand_center(self, s, i, j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return s[i+1:j]

    def longestPalindrome(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            tmp1 = self.expand_center(s, i, i)
            tmp2 = self.expand_center(s, i, i+1)
            if len(tmp1) > len(ans):
                ans = tmp1
            if len(tmp2) > len(ans):
                ans = tmp2
        return ans
        