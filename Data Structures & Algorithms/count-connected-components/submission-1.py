class Solution:
    def traverse(self, q, adj, visited):
        while q:
            node, parent = q.popleft()
            for nei in adj[node]:
                if nei == parent or visited[nei]:
                    continue
                visited[nei] = True
                q.append((nei, node))
    
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
                q.append((i, -1))
                visited[i] = True
                self.traverse(q, adj, visited)
        
        return ans

        