# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        #remove_from_beginning = length(head) - n
        dummy = ListNode(0,head)
        left = dummy
        right = head
        count = 0
        while count != n and right:
            count += 1
            right = right.next
        
        while right:
            left = left.next
            right = right.next
        left.next = left.next.next

        return dummy.next
        

        

        

            
        
        
