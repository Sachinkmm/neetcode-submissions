class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = [0] * 26
        for c in s:
            hash_map[ord(c) - ord('a')] += 1
        for c in t:
            hash_map[ord(c) - ord('a')] -= 1

        for val in hash_map:
            if val != 0:
                return False
        
        return True
