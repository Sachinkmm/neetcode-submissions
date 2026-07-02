"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def dfs(self, node):
        if node in self.oldToNew:
            return self.oldToNew[node]
        
        copy = Node(node.val)
        self.oldToNew[node] = copy
        for nbr in node.neighbors:
            copy.neighbors.append(self.dfs(nbr))
        
        return copy

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        self.oldToNew = {}
        if not node:
            return node
        return self.dfs(node)
        