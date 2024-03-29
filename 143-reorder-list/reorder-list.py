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
        1 -> 2 <- 3 <-  4
        s    f
             s           f
            
        1 -> 4 -> 2 -> 3


        1. find the middle node
        2. reverse the right nodes
        3. merge
        4. return head
        '''

        ret = ListNode(None, None)
        ret_p = ret # for adding the new node

        # 1. find the middle node
        s, f = head, head.next
        while f and f.next:
            s, f = s.next, f.next.next
        
        # 2. reverse the right nodes
        # 1<-2->3->4
        second = s.next
        s.next = None

        prev, p = None, second
        while p:
            tmp = p.next
            p.next = prev
            prev, p = p, tmp
        
        # 3. merge
        p1, p2 = head, prev

        while p1 and p2:
            tmp1, tmp2 = p1.next, p2.next

            ret_p.next = p1
            ret_p = ret_p.next

            ret_p.next = p2
            ret_p = ret_p.next

            p1, p2 = tmp1, tmp2

        while p1:
            tmp1 = p1.next
            ret_p.next = p1
            ret_p = ret_p.next

            p1 = tmp1

        return ret_p.next


            

        

        




        return ret.next