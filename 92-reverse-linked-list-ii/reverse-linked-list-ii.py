# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        start, end = None, None
        left_node, right_node = None, None
        dummy = ListNode()
        dummy.next = head

        p = dummy
        count = 0
        while p:
            if count == left-1:
                start = p
            if count == left:
                left_node = p
            if count == right:
                right_node = p
            if count == right+1:
                end = p
            count += 1
            p = p.next
        
        p_prev, p = None, left_node
        while p and p != right_node:
            tmp = p.next
            p.next = p_prev
            p_prev, p = p, tmp
        p.next = p_prev

        start.next = right_node
        left_node.next = end

        return dummy.next

        