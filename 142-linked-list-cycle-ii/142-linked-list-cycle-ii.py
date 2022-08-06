# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        
        visited = set()
        while p:
            if p in visited:
                return p
            visited.add(p)
            p = p.next
        
        return None