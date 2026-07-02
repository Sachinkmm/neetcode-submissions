class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans = 0
        # intervals.sort()
        # prevEnd = intervals[0][1]
        # for start, end in intervals[1:]:
        #     if start >= prevEnd:
        #         prevEnd = end
        #     else:
        #         ans += 1
        #         prevEnd = min(end, prevEnd)
        # return ans

        intervals.sort(key = lambda pair: pair[1])
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if prevEnd > start:
                ans += 1
            else:
                prevEnd = end
        return ans