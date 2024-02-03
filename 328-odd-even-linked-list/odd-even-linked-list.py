# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        example1.
            1 - > 2 -> 3 -> 4 -> 5
         head1   head2
            ^1    ^2
                       ^1   ^2   
                                 ^1  ^2


            ^1.next = head2

            1 -> 3 -> 5 -> 2 -> 4
        
        example2.
            1  -> 2
          head1   head2

        '''

        if not head or not head.next:
            return head
        
        head1, head2 = head, head.next

        p1, p2 = head1, head2
        while p2 and p2.next:
            p1.next = p1.next.next
            p2.next = p2.next.next

            p1 = p1.next
            p2 = p2.next
        
        p1.next = head2

        return head1
        
            
