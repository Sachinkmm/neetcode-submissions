class Solution:
    def binarySearch(self, val, intr):
        l, r = 0, len(intr) - 1
        ans = float('inf')
        while l <= r:
            mid = l + (r - l) // 2
            # if (val == 1):
            #     print(mid, intr[mid][0], intr[mid][1])
            if intr[mid][0] <= val and val <= intr[mid][1]:
                ans = min(ans, intr[mid][1] - intr[mid][0] + 1)
                l += 1
                r -= 1
            elif val < intr[mid][0]:
                r = mid - 1
            else:
                l = mid + 1
        return ans if ans != float('inf') else -1

    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        ans = []

        # for val in queries:
        #     dist = self.binarySearch(val, intervals)
        #     ans.append(dist)

        minHeap = []
        res = {}
        i = 0
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minHeap, (r - l + 1, r))
                i += 1
            
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            res[q] = minHeap[0][0] if minHeap else -1
        
        ans = [res[q] for q in queries]
        return ans

        