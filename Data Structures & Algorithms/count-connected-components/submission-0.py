class Solution:
    def traverse(self, q, adj, visited):
        while q:
            node, parent = q.popleft()
            for nei in adj[node]:
                if nei == parent or nei in visited:
                    continue
                visited.add(nei)
                q.append((nei, node))
    
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visited = set()
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        q = deque()
        ans = 0
        for i in range(n):
            if i not in visited:
                ans += 1
                q.append((i, -1))
                visited.add(i)
                self.traverse(q, adj, visited)
        
        return ans

        