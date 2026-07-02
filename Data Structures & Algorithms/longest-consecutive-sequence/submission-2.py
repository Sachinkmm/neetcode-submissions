class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        mp = defaultdict(int)

        # for num in nums:
        #     streak = 0
        #     curr = num
        #     while curr in store:
        #         curr += 1
        #         streak += 1
        #     ans = max(ans, streak)
        # return ans
        for num in nums:
            if not mp[num]:
                mp[num] = mp[num-1] + mp[num+1] + 1
                mp[num - mp[num-1]] = mp[num]
                mp[num + mp[num+1]] = mp[num]
                ans = max(ans, mp[num])
        return ans
        