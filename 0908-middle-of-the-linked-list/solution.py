# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fptr=head
        sptr=head
        while sptr and sptr.next:
            fptr=fptr.next
            sptr=sptr.next.next
        return fptr

        
