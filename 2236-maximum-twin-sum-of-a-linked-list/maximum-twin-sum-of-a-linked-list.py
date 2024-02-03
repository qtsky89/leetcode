# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        '''
        head = 10 -> 5 -> 4 -> 2 -> 1 -> 20

        ret = [10, 5, 4, 2, 1, 20]

        max(10 + 20, 5 + 1, 4+ 2) = > 30

        

        5 -> 4    2 -> 1
                  2 <- 1
        ^              ^

        step 1. find middle index
        step 2. reverse the right list
        step 3. get the maximum values
        '''

        # step 1. find middle index
        '''
        5 -> 4 -> 2 -> 1
        sf
             s    f
             sp   s      f
        '''
        
        slow_p_prev, slow_p, fast_p = head, head, head
        while fast_p and fast_p.next:
            slow_p_prev = slow_p
            slow_p = slow_p.next
            fast_p = fast_p.next.next
        
        slow_p_prev.next = None

        # step2 reverse the right list
        '''
        2 <- 1
        '''
        p_prev, p = None, slow_p

        while p:
            tmp = p.next
            p.next = p_prev
            p_prev, p = p, tmp
        
        # step 3
        max_val = -float('inf')
        p1, p2 = head, p_prev

        while p1 and p2:
            max_val = max(max_val, p1.val + p2.val)
            p1 = p1.next
            p2 = p2.next
        
        return max_val

        
        


