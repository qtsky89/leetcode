# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        1 -> 2 -> 3 -> 4 -> 5
        p1   p2

        1 -> 2 -> 3 -> 4
                  p1  p2
        
        1 -> 2
        p1   p2

        1
        
        None
        '''

        # dealt with edge cases
        if not head:
            return None
        if not head.next:
            return head
        
        p_prev , p = None, head
        while p:
            tmp = p.next
            p.next = p_prev
            p_prev, p = p, tmp
        return p_prev