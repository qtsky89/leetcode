# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        '''
        example1.
            5 -> 4 -> 10 <- 1 <- 20 <- 23
                                        ^    ^

            1. find the middle one
            2. after middle one reverse next pointer
            3. interate both list, update the maximum twin sum
            4. return that maximum twin sum
        '''

        s_prev, s, f = None, head, head

        # 1. find the middle one
        while f and f.next:
            s_prev, s, f = s, s.next, f.next.next
        
        # 2. after middle one reverse next pointer
        s_prev.next = None
        s_prev = None
        while s:
            tmp = s.next
            s.next = s_prev
            s_prev, s = s, tmp

        # 3. interate both list, update the maximum twin sum
        p1, p2 = head, s_prev

        max_twin_sum = 0
        while p1 and p2:
            max_twin_sum = max(max_twin_sum, p1.val + p2.val)
            p1, p2 = p1.next, p2.next
        
        return max_twin_sum