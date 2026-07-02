class Solution:
    def dfs(self, src, adj, res):
        while adj[src]:
            dst = adj[src].pop()
            self.dfs(dst, adj, res)
        res.append(src)

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in sorted(tickets)[::-1]:
            adj[src].append(dst)
        
        res = []
        self.dfs("JFK", adj, res)
        return res[::-1]
        