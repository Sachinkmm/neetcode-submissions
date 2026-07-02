class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, cost in flights:
            adj[u].append([v, cost])
    
        q = deque([src])
        wgt = [float('inf')] * n
        wgt[src] = 0

        while q:
            k -= 1
            length = len(q)
            while length > 0:
                length -= 1
                node = q.popleft()
                for v, cost in adj[node]:
                    print(v)
                    if k >= 0 or v == dst:
                        if (wgt[v] > cost + wgt[node]):
                            wgt[v] = cost + wgt[node]
                            q.append(v)
            if k < 0:
                return -1 if wgt[dst] == float('inf') else wgt[dst]
        return -1 if wgt[dst] == float('inf') else wgt[dst]
        