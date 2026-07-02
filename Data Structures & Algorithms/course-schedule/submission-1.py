class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        inbound = [0] * numCourses
        for i in range(len(prerequisites)):
            u, v = prerequisites[i][0], prerequisites[i][1]
            adj[v].append(u)
            inbound[u] += 1
        q = deque()
        for i in range(numCourses):
            if inbound[i] == 0:
                q.append(i)
        res = []
        while q:
            length = len(q)
            node = q.popleft()
            res.append(node)
            for i in range(len(adj[node])):
                v = adj[node][i]
                inbound[v] -= 1
                if inbound[v] == 0:
                    q.append(v)
        return True if len(res) == numCourses else False

        