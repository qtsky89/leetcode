# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        '''

        1 -> 2 -> 3          4 <- 5
        ^                         ^


        1 -> 5 -> 2-> 4 -> 3

        '''

        if not head.next:
            return head

        # find middle position
        s, f = head, head.next
        
        while f and f.next:
            s = s.next
            f = f.next.next
        
        tmp = s.next
        s.next = None
        
        # right nodes, change direction
        prev, p = None, tmp
        while p:
            tmp = p.next
            p.next = prev

            prev, p = p, tmp
        
        # merge
        p1, p2 = head, prev
        
        while p1 and p2:
            p1_next, p2_next = p1.next, p2.next

            p1.next, p2.next = p2, p1.next

            p1, p2 = p1_next, p2_next