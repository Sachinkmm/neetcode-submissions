class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isLast = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        ptr = self.root
        for c in word:
            i = ord(c) - ord('a')
            if not ptr.children[i]:
                ptr.children[i] = TrieNode()
            ptr = ptr.children[i]
        ptr.isLast = True

    def search(self, word: str) -> bool:
        ptr = self.root
        for c in word:
            i = ord(c) - ord('a')
            if not ptr.children[i]:
                return False
            ptr = ptr.children[i]
        return ptr.isLast

    def startsWith(self, prefix: str) -> bool:
        ptr = self.root
        for c in prefix:
            i = ord(c) - ord('a')
            if not ptr.children[i]:
                return False
            ptr = ptr.children[i]
        return True
        
        