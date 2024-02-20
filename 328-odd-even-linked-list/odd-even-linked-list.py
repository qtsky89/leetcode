# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        example1.

        ret -> 0 ->
        output: 0 -> 2 -> 4 -> 1 -> 3

        input:  0 -> 1 -> 2 -> 3 -> 4
                ^1   ^2
                          ^1   ^2
        output: 0 -> 2 -> 4 -> 1 -> 3

        example2.
        input:  0
        output: 0

        example3.
        input:  0 -> 1
        output: 0 -> 1

        example4.
        input:  0 -> 1 -> 2
                ^    ^
                          ^   ^
         
        output: 0 -> 2 -> 1

        example5.
        input:  0 -> 1 -> 2 -> 3
                ^    ^
                          ^    ^

        output: 0 -> 2 -> 1 -> 3
        '''

        if not head:
            return None

        tmp = head.next
        p1, p2 = head, head.next

        while p2 and p2.next:
            p1.next, p2.next = p1.next.next, p2.next.next
            p1, p2 = p1.next, p2.next
        
        p1.next = tmp

        return head

