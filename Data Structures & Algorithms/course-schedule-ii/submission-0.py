class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        inDegree = [0] * numCourses
        for u, v, in prerequisites:
            adj[v].append(u)
            inDegree[u] += 1
        
        q = deque()
        for i in range(numCourses):
            if inDegree[i] == 0:
                q.append(i)
            
        res = []
        while q:
            node = q.popleft()
            res.append(node)
            for v in adj[node]:
                inDegree[v] -= 1
                if inDegree[v] == 0:
                    q.append(v)
        
        return res if len(res) == numCourses else []
        