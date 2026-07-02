class Solution:
    def dfs(self, node, par, visit, adj, cycle):
        if visit[node]:
            self.cycleStart = node
            return True
        
        visit[node] = True
        for nei in adj[node]:
            if nei == par:
                continue
            if self.dfs(nei, node, visit, adj, cycle):
                if self.cycleStart != -1:
                    cycle.add(node)
                if node == self.cycleStart:
                    self.cycleStart = -1
                return True
        return False

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visit = [False] * (n + 1)
        cycle = set()
        self.cycleStart = -1
        
        self.dfs(1, -1, visit, adj, cycle)

        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u, v]

        