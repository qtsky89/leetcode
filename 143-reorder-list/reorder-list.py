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
        1 -> 2 -> 3 <- 4 <- 5
        ^         ^         ^
    
        1. find the middle man
        2. after middle man change direction
        3. merge!


        1 -> 2 -> 3 <- 4
                  ^

        1 -> 4 -> 2 -> 3 -> None
        '''

        # 1. find the middle man

        s, f = head, head.next
        while f and f.next:
            s = s.next
            f = f.next.next
        
        # 2. after middle man change direction
        prev, p = None, s

        while p:
            tmp = p.next
            p.next = prev
            prev, p = p, tmp

        
        # 3. merge!
        p1, p2 = head, prev
        
        while p1 and p2:
            tmp1, tmp2 = p1.next, p2.next
            
            p1.next, p2.next = p2, tmp1

            p1, p2 = tmp1, tmp2
        
        return head
        
        
        

        