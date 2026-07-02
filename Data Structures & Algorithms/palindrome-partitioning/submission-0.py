class Solution:
    def isPalin(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def dfs(self, idx, s, part, res):
        if idx == len(s):
            res.append(part.copy())
            return
        
        for j in range(idx, len(s)):
            if self.isPalin(s, idx, j):
                part.append(s[idx : j + 1])
                self.dfs(j + 1, s, part, res)
                part.pop()

    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        self.dfs(0, s, part, res)
        return res
        
        