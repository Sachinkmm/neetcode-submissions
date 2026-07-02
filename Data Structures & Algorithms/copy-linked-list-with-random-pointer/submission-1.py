"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        ptr = head
        while ptr:
            node = Node(ptr.val, ptr.next, ptr.random)
            ptr.next = node
            ptr = node.next
        ptr = head
        while ptr:
            if ptr.random:
                ptr.next.random = ptr.random.next
            ptr = ptr.next.next
        
        ptr = head
        nhead = ptr.next
        ptr2 = nhead
        
        while ptr and ptr.next:
            ptr.next = ptr2.next
            if ptr.next:
                ptr = ptr.next
                ptr2.next = ptr.next
                ptr2 = ptr2.next

        return nhead
        