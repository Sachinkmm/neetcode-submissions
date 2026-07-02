class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        if n == 0:
            return [newInterval]
        ans = []
        for i in range(n):
            if not newInterval:
                if ans[-1][1] >= intervals[i][0]:
                    ans[-1][1] = max(ans[-1][1], intervals[i][1])
                else:
                    ans.append(intervals[i])
            else:
                if newInterval[0] <= intervals[i][1]:
                    if (newInterval[1] < intervals[i][0]):
                        ans.append(newInterval)
                    else:
                        intervals[i][1] = max(intervals[i][1], newInterval[1])
                        intervals[i][0] = min(intervals[i][0], newInterval[0])
                    newInterval = None
                ans.append(intervals[i])
                if i == n-1 and newInterval:
                    ans.append(newInterval)
        
        return ans