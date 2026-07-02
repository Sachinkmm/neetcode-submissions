# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head, k):
        ptr = head
        prev = None
        while k > 0 and ptr:
            tmp = ptr
            ptr = ptr.next
            tmp.next = prev
            prev = tmp
            k -= 1
        return prev
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        ptr = dummy
        lastNode = head
        while lastNode:
            n = k
            ptr1 = lastNode
            while n > 0 and ptr1:
                ptr1 = ptr1.next
                n -= 1
            if not ptr1 and n > 0:
                ptr.next = lastNode
                return dummy.next
            ptr.next = self.reverse(lastNode, k)
            ptr = lastNode
            lastNode = ptr1
        return dummy.next
        