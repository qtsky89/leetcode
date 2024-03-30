# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_stack, l2_stack = [], []

        p = l1
        while p:
            l1_stack.append(p.val)
            p = p.next
        
        p = l2
        while p:
            l2_stack.append(p.val)
            p = p.next
        
        ret = None

        carry = 0
        while l1_stack and l2_stack:
            op1, op2 = l1_stack.pop(), l2_stack.pop()

            tmp = op1 + op2 + carry
            carry = 0
            if tmp >= 10:
                tmp -= 10
                carry = 1
            
            new_node = ListNode(tmp)
            new_node.next = ret
            ret = new_node
        
        while l1_stack:
            tmp = l1_stack.pop() + carry
            carry = 0
            if tmp >= 10:
                tmp -= 10
                carry = 1
            
            new_node = ListNode(tmp)
            new_node.next = ret
            ret = new_node

        while l2_stack:
            tmp = l2_stack.pop() + carry
            carry = 0
            if tmp >= 10:
                tmp -= 10
                carry = 1
            
            new_node = ListNode(tmp)
            new_node.next = ret
            ret = new_node
        
        if carry == 1:
            new_node = ListNode(1)
            new_node.next = ret
            ret = new_node

        return ret
