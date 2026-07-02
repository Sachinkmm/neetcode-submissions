class Solution:
    def recur(self, i, j, k, s1, s2, s3, dp):
        if k == len(s3):
            return i == len(s1) and j == len(s2)
        
        if (i, j) in dp:
            return dp[(i, j)]
        
        res = False
        if i < len(s1) and s1[i] == s3[k]:
            res = self.recur(i + 1, j, k + 1, s1, s2, s3, dp)
        
        if not res and j < len(s2) and s2[j] == s3[k]:
            res = self.recur(i, j + 1, k + 1, s1, s2, s3, dp)
        
        dp[(i, j)] = res
        
        return res

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = {}
        return self.recur(0, 0, 0, s1, s2, s3, dp)
        