# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr = head
        while n > 0:
            n -= 1
            ptr = ptr.next
        if not ptr:
            return head.next
        tmp = head
        prev = None
        while ptr:
            prev = tmp
            tmp = tmp.next
            ptr = ptr.next
        prev.next = tmp.next
        return head
        