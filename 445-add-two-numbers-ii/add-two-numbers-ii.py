# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        7 -> 2 -> 4 -> 3
             5 -> 6 -> 4

        3 -> 4 -> 2 -> 7
        4 -> 6 -> 5

        7 -> 0 -> 8 -> 7 reverse again!
        '''
    
        l1_reversed = self.reverse(l1)
        l2_reversed = self.reverse(l2)

        ret = ListNode(None)
        p = ret

        p1, p2 = l1_reversed, l2_reversed

        carry = 0
        while p1 and p2:
            tmp = p1.val + p2.val + carry

            if tmp >= 10:
                carry = 1
                tmp -= 10
            else:
                carry = 0

            p.next = ListNode(tmp)
            p = p.next
            p1 = p1.next
            p2 = p2.next
        
        while p1:
            tmp = p1.val + carry
            if tmp >= 10:
                carry = 1
                tmp -= 10
            else:
                carry = 0
            
            p.next = ListNode(tmp)
            p = p.next
            p1 = p1.next

        while p2:
            tmp = p2.val + carry
            if tmp >= 10:
                carry = 1
                tmp -= 10
            else:
                carry = 0
            
            p.next = ListNode(tmp)
            p = p.next
            p2 = p2.next
        
        if carry == 1:
            p.next = ListNode(1)
            carry = 0
        
        return self.reverse(ret.next)

    def reverse(self, head: ListNode) -> ListNode:
        prev, p = None, head

        while p:
            tmp = p.next
            p.next = prev
            prev, p = p, tmp
        
        return prev
        


