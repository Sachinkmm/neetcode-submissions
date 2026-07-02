class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        ans = []

        for st in strs:
            hmp = [0] * 26
            for ch in st:
                hmp[ord(ch) - ord('a')] += 1
            cnt_tuple = tuple(hmp)
            if cnt_tuple not in mp:
                mp[cnt_tuple] = []
            mp[cnt_tuple].append(st)
        
        for key, val in mp.items():
            ans.append(val)
        
        return ans