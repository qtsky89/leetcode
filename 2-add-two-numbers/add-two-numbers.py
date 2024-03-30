# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = l1, l2

        ret = ListNode(None)
        p3 = ret

        carry = 0
        while p1 and p2:
            tmp = p1.val + p2.val + carry
            carry = 0

            if tmp >= 10:
                tmp -= 10
                carry = 1
            
            p3.next = ListNode(tmp)
            p3 = p3.next

            p1, p2 = p1.next, p2.next
        
        while p1:
            tmp = p1.val + carry
            carry = 0
            if tmp >= 10:
                tmp -= 10
                carry = 1
            p3.next = ListNode(tmp)
            p3 = p3.next

            p1 = p1.next
        
        while p2:
            tmp = p2.val + carry
            carry = 0
            if tmp >= 10:
                tmp -= 10
                carry = 1
            p3.next = ListNode(tmp)
            p3 = p3.next

            p2 = p2.next
        
        if carry:
            p3.next = ListNode(carry)
            carry = 0
            p3 = p3.next
        return ret.next
            
