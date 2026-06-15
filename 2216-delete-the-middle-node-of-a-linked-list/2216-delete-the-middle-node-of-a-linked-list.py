# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tor, rab = head, head
        midLeft, midRight = head, head
        while rab is not None and rab.next is not None:
            midLeft = tor
            tor = tor.next
            rab = rab.next.next
        midRight = tor.next
        if tor == midLeft:
            return None
        midLeft.next = midRight
        return head
