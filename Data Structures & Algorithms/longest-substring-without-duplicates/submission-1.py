class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        mp = defaultdict(int)
        l = 0
        r = 0
        ans = 0
        while r < n:
            if s[r] in mp:
                l = max(l, mp[s[r]] + 1)
            mp[s[r]] = r
            print(l, " ", r)
            ans = max(ans, r - l + 1)
            r += 1
        return ans