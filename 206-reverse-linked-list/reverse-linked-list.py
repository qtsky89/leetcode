# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        head =   1 -> 2 -> 3-> 4 -> 5
                 p   p_n
                                    p  p_n

        result=  1 <- 2 <- 3 <- 4 <- 5
                                     ^
        return 5
        '''

        if not head:
            return

        p, p_n = None, head

        while p_n:
            tmp = p_n.next
            p_n.next = p

            p, p_n = p_n, tmp
        return p
