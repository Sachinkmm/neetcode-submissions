class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        visited = set()

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        q = deque([(0, -1)])
        visited.add(0)

        while q:
            u, parent = q.popleft()
            for v in adj[u]:
                if v == parent:
                    continue
                if v in visited:
                    return False
                q.append((v, u))
                visited.add(v)
        
        return len(visited) == n