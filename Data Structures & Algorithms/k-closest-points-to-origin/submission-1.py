class Solution:
    def distanceFromOrigin(self, x, y):
        return round(math.sqrt(x ** 2 + y ** 2), 1)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        for i in range(len(points)):
            distance = self.distanceFromOrigin(points[i][0], points[i][1])
            heapq.heappush(pq, (-1*distance, i))
            if len(pq) > k:
                heapq.heappop(pq)
        ans = []
        for dis, i in pq:
            ans.append(points[i])
        return ans