class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n + 1)]
        visited = [float("inf")] * (n + 1)

        for u, v, t in times:
            adj[u].append([v, t])
        
        visited[k] = 0
        visited[0] = 0

        q = deque([k])
        while q:
            node = q.popleft()
            for v, t in adj[node]:
                if visited[v] > visited[node] + t:
                    visited[v] = visited[node] + t
                    q.append(v)
        
        return max(visited) if max(visited) !=  float("inf") else -1
        