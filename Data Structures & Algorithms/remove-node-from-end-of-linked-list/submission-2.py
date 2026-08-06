# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = prev = ListNode()
        count = 0
        prev.next = head
        cur = head
        length = 0
        while cur.next:
            cur = cur.next
            length += 1

        while count != length + 1 - n and head.next:
            head = head.next
            prev = prev.next
            count += 1
        
        prev.next = head.next
        return dummy.next
