class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        for val in nums:
            heapq.heappush(pq, val)
            if len(pq) > k:
                heapq.heappop(pq)
            
        return pq[0]