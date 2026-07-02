class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.idx = -1
        self.refs = 0
    
    def addWord(self, word, i):
        ptr = self
        ptr.refs += 1
        for c in word:
            idx = ord(c) - ord('a')
            if not ptr.children[idx]:
                ptr.children[idx] = TrieNode()
            ptr = ptr.children[idx]
            ptr.refs += 1
        ptr.idx = i

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for i in range(len(words)):
            root.addWord(words[i], i)
        
        rows, cols = len(board), len(board[0])
        res = []

        def getIndex(c):
            return ord(c) - ord('a')
        
        def dfs(r, c, node):
    
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] == '*' or not node.children[getIndex(board[r][c])]:
                return
            
            idx = getIndex(board[r][c])
            tmp = board[r][c]
            board[r][c] = '*'
            prev = node
            node = node.children[idx]
            if node.idx != -1:
                res.append(words[node.idx])
                node.idx = -1
                node.refs -= 1
                if not node.refs:
                    prev.children[idx] = None
                    node = None
                    board[r][c] = tmp
                    return
            dfs(r + 1, c, node)
            dfs(r - 1, c, node)
            dfs(r, c + 1, node)
            dfs(r, c - 1, node)

            board[r][c] = tmp
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)
        
        return res
        