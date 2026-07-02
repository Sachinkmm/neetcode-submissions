class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = []
        for val in stones:
            val = -1 * val
            heapq.heappush(pq, val)
        while len(pq) > 1:
            stone1 = heapq.heappop(pq)
            stone2 = heapq.heappop(pq)
            if stone1 < stone2:
                heapq.heappush(pq, stone1 - stone2)
        
        pq.append(0)
        return abs(pq[0])
        