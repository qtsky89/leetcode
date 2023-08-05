# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        1 -> 2 -> 3 -> 4 -> 5
                            p1   p2

        1 -> 3-> 5 -> 2 -> 4



        1-> 2-> 3-> 4
        p1  p2
                p1  p2

        
        1 -> 2 -> 3
                 p1   p2
        '''

        if head is None:
            return None
        if head.next is None:
            return head
        
        second_head = head.next
        p1, p2 = head, head.next
        while p2 and p2.next:
            p1.next = p1.next.next if p1.next else None
            p2.next = p2.next.next if p2.next else None
            p1, p2 = p1.next, p2.next
        

        p1.next = second_head

        return head

        
        

        












