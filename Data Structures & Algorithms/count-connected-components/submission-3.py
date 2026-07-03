class Solution:
    def traverse(self, q, adj, visited):
        while q:
            u = q.popleft()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visited = [False] * n

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        q = deque()
        ans = 0

        for u in range(n):
            if not visited[u]:
                q.append(u)
                ans += 1
                visited[u] = True
                self.traverse(q, adj, visited)
        
        return ans