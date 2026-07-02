class Solution:
    def traverse(self, q, adj, visited):
        while q:
            node = q.popleft()
            for nei in adj[node]:
                if not visited[nei]:
                    visited[nei] = True
                    q.append(nei)
    
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visited = [False] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        q = deque()
        ans = 0
        for i in range(n):
            if not visited[i]:
                ans += 1
                q.append(i)
                visited[i] = True
                self.traverse(q, adj, visited)
        
        return ans

        