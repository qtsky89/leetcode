# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        '''
        '''

        dummy = ListNode(None)
        dummy.next = head

        count = 0

        nodes = [None] * 4
        p = dummy
        while p:
            if count == left-1:
                nodes[0] = p
            if count == left:
                nodes[1] = p
            if count == right:
                nodes[2] = p
            if count == right+1:
                nodes[3] = p

            count += 1
            p = p.next
        
        # reverse
        prev, p = None, nodes[1]
        while p != nodes[3]:
            tmp = p.next

            p.next = prev

            prev, p = p, tmp
        
        nodes[0].next, nodes[1].next = nodes[2], nodes[3]

        return dummy.next