class Solution:

    def recur(self, i, j, w1, w2):
        if i < 0:
            return j + 1
        if j < 0:
            return i + 1
        
        ans = float('inf')
        if w1[i] == w2[j]:
            ans = self.recur(i-1, j-1, w1, w2)
        else:
            insert = self.recur(i, j-1, w1, w2)
            dele = self.recur(i-1, j, w1, w2)
            rep = self.recur(i-1, j-1, w1, w2)
            ans = 1 + min(insert, dele, rep)
        
        return ans

    def minDistance(self, word1: str, word2: str) -> int:
        lw1 = len(word1)
        lw2 = len(word2)

        return self.recur(lw1 - 1, lw2 - 1, word1, word2)