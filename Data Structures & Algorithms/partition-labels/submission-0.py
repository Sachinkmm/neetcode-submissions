class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mp = [0] * 26
        for i in range(len(s)):
            mp[ord(s[i]) - ord('a')] = i

        res = []
        l = r = 0
        for i in range(len(s)):
            if mp[ord(s[i]) - ord('a')] == r and i == r:
                res.append(i - l + 1)
                l = r = i + 1
            else:
                r = max(r, mp[ord(s[i]) - ord('a')])
        return res