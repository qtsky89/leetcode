# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        example1.
        
        head = 0 -> 1 -> 4 -> 7 -> 1 -> 2 -> 6
              ^^
                    ^    ^
                         ^         ^
                              ^              ^
        

        head = 1 -> 2 -> 3 -> 4
               ^^
                    ^    ^
                         ^        ^

        
        head = 2 -> 1
               ^^
                    ^   ^

        ending term.    
            fast pointer ==> None
            fast pointer ==> end index

        remove slow pointer ( to do that we need to keep slow_prev_pointer )

        middle_index = (len(head)) // 2 

        '''

        if head is None or head.next is None:
            return None
        
        slow_prev_p, slow_p, fast_p = head, head, head

        while fast_p and fast_p.next:
            slow_prev_p, slow_p = slow_p, slow_p.next
            fast_p = fast_p.next.next
        
        slow_prev_p.next = slow_p.next

        return head

