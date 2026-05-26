# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0: # right is n places ahead of left (start)
            right = right.next
            n -= 1
        
        while right: # Increment both left and right until right is at the end
                     # This means that left is just before the point that needs to be removed
            left = left.next
            right = right.next

        left.next = left.next.next # Set left to skip node, effectively removing it

        return dummy.next