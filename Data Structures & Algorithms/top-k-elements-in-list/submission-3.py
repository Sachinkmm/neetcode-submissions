class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        for num in nums:
            if num not in mp:
                mp[num] = 0
            mp[num] += 1
        
        max_heap = []
        for key, val in mp.items():
            heapq.heappush(max_heap, (val, key))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        ans = []
        while k > 0:
            ans.append(max_heap[0][1])
            heapq.heappop(max_heap)
            k -= 1
        
        return ans