# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        s, f = head, head.next

        while f and f.next:
            if s == f:
                return True

            s, f = s.next, f.next.next

        return False