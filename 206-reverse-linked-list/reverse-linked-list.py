# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p_prev, p = None, head

        while p:
            tmp = p.next
            p.next = p_prev
            p_prev, p = p, tmp
        
        return p_prev