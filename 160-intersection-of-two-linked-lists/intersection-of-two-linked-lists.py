# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visited = set()

        p = headA
        
        while p:
            visited.add(p)
            p = p.next
        
        p  = headB
        while p:
            if p in visited:
                return p
            p = p.next
        
        return None