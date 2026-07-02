class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cacheMap = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cacheMap:
            return -1
        node = self.cacheMap[key]
        self.remove(node)
        self.add(node)
        return node.val
    
    def remove(self, node):
        prev = node.prev
        prev.next = node.next
        node.next.prev = prev
    
    def add(self, node):
        tmp = self.head.next
        node.next = tmp
        tmp.prev = node
        self.head.next = node
        node.prev = self.head

    def put(self, key: int, value: int) -> None:
        node = None
        if key in self.cacheMap:
            node = self.cacheMap[key]
            node.val = value
            self.remove(node)
        else:
            node = Node(key, value)
            self.cacheMap[key] = node
        self.add(node)
        if len(self.cacheMap) > self.capacity:
            node = self.tail.prev
            self.remove(node)
            del self.cacheMap[node.key]
        
