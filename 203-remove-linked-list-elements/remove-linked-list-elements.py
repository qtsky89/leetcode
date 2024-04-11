# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        '''
        dummy 1 2 6  6  3 4 5 6
             prev p

        '''

        dummy = ListNode(None)
        dummy.next = head

        prev, p = dummy, head

        while p:
            if p.val == val:
                prev.next = p.next
                p = p.next
            else:
                prev, p = p, p.next
        
        return dummy.next
            