class Solution:
    def recur(self, i, j, k, s1, s2, s3):
        if k == len(s3):
            return i == len(s1) and j == len(s2)
        
        if i < len(s1) and s1[i] == s3[k]:
            if self.recur(i + 1, j, k + 1, s1, s2, s3):
                return True
        
        if j < len(s2) and s2[j] == s3[k]:
            if self.recur(i, j + 1, k + 1, s1, s2, s3):
                return True
        
        return False

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        return self.recur(0, 0, 0, s1, s2, s3)
        