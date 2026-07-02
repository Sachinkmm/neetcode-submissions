class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = [0] * 26
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            hash_map[ord(s[i]) - ord('a')] += 1
            hash_map[ord(t[i]) - ord('a')] -= 1

        for val in hash_map:
            if val != 0:
                return False
        
        return True
