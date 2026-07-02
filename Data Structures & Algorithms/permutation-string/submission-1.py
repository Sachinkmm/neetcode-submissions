class Solution:
    def checkContains(self, s1, s2, idx):
        mp = [0]*26
        for i in range(len(s1)):
            mp[ord(s1[i]) - ord('a')] += 1
        for i in range(idx, idx+len(s1)):
            mp[ord(s2[i]) - ord('a')] -= 1
        return all(i == 0 for i in mp)

    def checkInclusion(self, s1: str, s2: str) -> bool:
        # O (s1 * s2)
        # if len(s1) > len(s2):
        #     return False
        # n = len(s2)
        # for i in range(0, n-len(s1)+1):
        #     if self.checkContains(s1, s2, i):
        #         return True
        # return False
        if len(s1) > len(s2):
            return False
        countS1 = [0] * 26
        countS2 = [0] * 26
        for i in range(len(s1)):
            countS1[ord(s1[i]) - ord('a')] += 1
            countS2[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            if countS1[i] == countS2[i]:
                matches += 1
        
        l = 0
        for i in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            idx = ord(s2[i]) - ord('a')
            countS2[idx] += 1
            if countS1[idx] == countS2[idx]:
                matches += 1
            elif countS1[idx] + 1 == countS2[idx]:
                matches -= 1
            
            idx = ord(s2[l]) - ord('a')
            countS2[idx] -= 1
            if countS1[idx] == countS2[idx]:
                matches += 1
            elif countS1[idx] - 1 == countS2[idx]:
                matches -= 1
            l += 1
        return matches == 26
        