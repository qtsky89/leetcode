# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # list =   1 3 4 7 1 2 6
        # return = 1 3 4 1 2 6

        # list = 1 2 3 4
        # return = 1 2 4

        # list = 2 1
        # return 1

        # list = 1
        # return = null ?

        # list = 1 2 3 4 5
        # return = 1 2 4 5

        # 1. find middle node
        # 2. remove middle node
    
        if head is None or head.next is None:
            return None

        # list len size >= 2
        middle_node = self._get_middle_node(head)
        self._remove_middle_node(head, middle_node)
        return head

    
    # 1. find middle node
    # list = 1 3 4 7 1 2 6
    #        sf
    #          s f
    #            s   f
    #              s     f

    # list = 1 3 4 7 1 2
    #        sf
    #          s f
    #            s   f
    #              s     f

    # list = 1 2
    #        sf
    #          s f
    def _get_middle_node(self, head: ListNode) -> ListNode:
        s, f = head, head

        while not (f is None or f.next is None):
            s = s.next
            f = f.next.next
        
        return s
    
    # 2. remove middle node
    # list =  1   3
    #         p
    def _remove_middle_node(self, head: ListNode, middle_node: ListNode):
        p = head
        while p:
            if p.next is middle_node:
                p.next = middle_node.next
            p = p.next

    
