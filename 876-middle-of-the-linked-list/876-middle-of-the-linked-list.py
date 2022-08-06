# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 1 -> 2 -> 3 -> 4 -> 5
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        
        s, f = head, head
        
        while f and f.next:
            s = s.next
            f = f.next.next
        
        return s