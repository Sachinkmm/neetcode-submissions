class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isLast = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        ptr = self.root
        for c in word:
            i = ord(c) - ord('a')
            if not ptr.children[i]:
                ptr.children[i] = TrieNode()
            ptr = ptr.children[i]
        ptr.isLast = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            if not root:
                return False
            ptr = root
            
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in ptr.children:
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    idx = ord(c) - ord('a')
                    if not ptr.children[idx]:
                        return False
                    ptr = ptr.children[idx]
            return ptr.isLast

        return dfs(0, self.root)
