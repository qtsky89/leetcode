# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None

        dummy = ListNode(val=None, next=head)

        prev, p1 = dummy, head

        p2 = head
        while n > 0:
            p2 = p2.next
            n -= 1
        
        '''
        1  2  3  4  5
            prev p1   p2
        '''

        while p2:
            prev, p1, p2 = p1, p1.next, p2.next

        prev.next = p1.next

        return dummy.next
