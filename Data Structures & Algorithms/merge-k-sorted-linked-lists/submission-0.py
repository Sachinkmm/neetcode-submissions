# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeList(self, l1, l2):
        head = ListNode()
        ptr = head
        ptr1 = l1
        ptr2 = l2
        while ptr1 and ptr2:
            if ptr1.val < ptr2.val:
                ptr.next = ptr1
                ptr1 = ptr1.next
            else:
                ptr.next = ptr2
                ptr2 = ptr2.next
            ptr = ptr.next
        if ptr1:
            ptr.next = ptr1
        if ptr2:
            ptr.next = ptr2
        return head.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if n == 0:
            return None
        ptr = lists[0]
        for i in range(1, n):
            print(ptr.val)
            ptr = self.mergeList(ptr, lists[i])
        return ptr
        