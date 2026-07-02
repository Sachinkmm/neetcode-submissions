class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        ans = []
        intervals.sort()
        for inter in intervals:
            if ans and ans[-1][1] >= inter[0]:
                ans[-1][1] = max(ans[-1][1], inter[1])
            else:
                ans.append(inter)
        return ans
        