# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
     None ->  1 -> 2 -> 3-> 4 -> 5
        ^ <- ^
                             ^ <- ^
                                  ^ <- ^

        5 -> 4 -> 3 -> 2 -> 1
        ^
        '''

        prev, p = None, head
        
        while p:
            tmp = p.next
            p.next = prev
            prev, p = p, tmp
        
        return prev

