# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals=[]
        c=head
        while c!=None:
            vals.append(c.val)
            c=c.next
        if vals==vals[::-1]:
            return True
        else:
            return False
