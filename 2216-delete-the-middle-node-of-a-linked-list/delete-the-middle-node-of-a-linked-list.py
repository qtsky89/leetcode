# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        example1. 0                 => None
        example2. 0 -> 1            => 0
                       ^
        example3. 0 -> 1 -> 2       => 0 -> 2
                       ^
        example4. 0 -> 1 -> 2 -> 3  => 0 -> 1 -> 3
                            ^

                  0 -> 1 -> 2 -> 3
                  ^ ^
                       ^    ^
                            ^      ^
                       
                     
                
            dummy->0 -> 1 -> 2 -> 3 -> 4
                ^ ^^
                       ^    ^
                            ^         ^
        '''

        dummy = ListNode(None, None)
        dummy.next = head

        slow_prev, slow, fast = dummy, head, head
        
        while fast and fast.next:
            slow_prev, slow, fast = slow, slow.next, fast.next.next
        
        # slow is the one we want to delete
        slow_prev.next = slow.next

        return dummy.next



        

        