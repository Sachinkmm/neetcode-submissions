class Solution:
    def recur(self, i, s, wordDict):
        if i in self.memo:
            return self.memo[i]
        
        for w in wordDict:
            if (i + len(w) <= len(s) and s[i : i + len(w)] == w):
                if self.recur(i+len(w), s, wordDict):
                    self.memo[i] = True
                    return True
        self.memo[i] = False
        return False

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.memo = {len(s) : True}
        return self.recur(0, s, wordDict)
        