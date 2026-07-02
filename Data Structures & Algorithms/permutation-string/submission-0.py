class Solution:
    def checkContains(self, s1, s2, idx):
        mp = [0]*26
        for i in range(len(s1)):
            mp[ord(s1[i]) - ord('a')] += 1
        for i in range(idx, idx+len(s1)):
            mp[ord(s2[i]) - ord('a')] -= 1
        return all(i == 0 for i in mp)

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        n = len(s2)
        for i in range(0, n-len(s1)+1):
            if self.checkContains(s1, s2, i):
                return True
        return False
        