class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = [0] * 26
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            idx = ord(s[i]) - ord('a')
            s_map[idx] += 1
            idx = ord(t[i]) - ord('a')
            s_map[idx] -= 1
        
        for val in s_map:
            if val != 0:
                return False
        
        return True
