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
        

        1 -> 2 -> 3 -> 4 -> 5-> None  None<- 6 <- 7 <- 8 <- 9 <- 10
        h    s                                        f

        1 -> 2 -> 10 -> 3 -> 8 ->  4 -> 7 -> 5 -> 6                   


        1 -> 10 -> 2 -> 9 -> 3 -> 8 -> 4 -> 7 -> 5 -> 6
        '''


        '''
        1 -> 2-> 3-> 4 -> 5 -> None, None<-6 <- 7 <-  8 <- 9 <- 10
        p1                                                      p2

        1 -> 10 -> 2


        1 -> 2 -> 3
        s    f
        '''


        s,f  = head, head.next

        while f and f.next:
            s, f = s.next, f.next.next

        
        tmp = s.next
        s.next = None
        
        prev, p = None, tmp

        while p:
            tmp = p.next
            p.next = prev
            prev, p = p, tmp

        
        p1, p2 = head, prev

        while p1 and p2:
            tmp1 = p1.next
            tmp2 = p2.next

            p1.next, p2.next = p2, p1.next

            p1,p2 = tmp1, tmp2
        
        

        
        
        
