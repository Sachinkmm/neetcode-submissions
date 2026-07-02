class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        mp = {}
        ans = []
        for st in strs:
            count = [0] * 26
            for ch in st:
                count[ord(ch) - ord('a')] += 1
            count_tuple = tuple(count)
            if count_tuple not in mp:
                mp[count_tuple] = []
            mp[count_tuple].append(st)
        for key, values in mp.items():
            ans.append(values)
        return ans

        