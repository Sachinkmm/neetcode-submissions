class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = []
        for val in stones:
            val = -1 * val
            heapq.heappush(pq, val)
        while len(pq) > 1:
            stone1 = -1 * heapq.heappop(pq)
            stone2 = -1 * heapq.heappop(pq)
            if stone1 == stone2:
                continue
            else:
                val = -1 * (stone1 - stone2)
                heapq.heappush(pq, val)
        
        if not pq:
            return 0
        return -1 * (pq[0])
        