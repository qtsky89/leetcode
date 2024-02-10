# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        3 -> 2 -> 0 -> -4
        sf

        1. if no cycle, s, f are not going to meet

        2. if cycle, s, f will be meet
        '''

        if not head:
            return False
        
        s, f = head, head.next

        while f and f.next:
            if s == f:
                return True
            s, f = s.next, f.next.next
        return False
        

        