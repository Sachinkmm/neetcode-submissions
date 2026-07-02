class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = [[] for _ in range(n)]
        for u, v, p in flights:
            adj_list[u].append([v, p])
        
        wgt = [float('inf')] * n
        wgt[src] = 0

        q = deque([(0, src, 0)]) # (stop, source, dist)

        while q:
            stop, node, dist = q.popleft()
            if stop > k:
                continue
            
            for v, wt in adj_list[node]:
                if dist + wt < wgt[v]:
                    wgt[v] = dist + wt
                    q.append([stop + 1, v, dist + wt])
        
        return -1 if wgt[dst] == float('inf') else wgt[dst]
        