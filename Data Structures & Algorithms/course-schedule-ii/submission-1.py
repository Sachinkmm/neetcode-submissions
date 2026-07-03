class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        inDegree = [0] * numCourses

        for u, v in prerequisites:
            adj[v].append(u)
            inDegree[u] += 1
        
        q = deque()

        for u in range(numCourses):
            if inDegree[u] == 0:
                q.append(u)
        
        res = []
        while q:
            u = q.popleft()
            res.append(u)
            for v in adj[u]:
                inDegree[v] -= 1
                if inDegree[v] == 0:
                    q.append(v)
        
        if len(res) == numCourses:
            return res
        return []