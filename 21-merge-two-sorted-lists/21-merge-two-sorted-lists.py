# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class List:
    def __init__(self):
        self.head = ListNode()
        self.tail = self.head
    
    def add_node(self, new_node: ListNode):
        self.tail.next = new_node
        self.tail = self.tail.next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        ret = List()
        
        p1, p2 = list1, list2
        
        while p1 and p2:
            if p1.val >= p2.val:
                ret.add_node(p2)
                p2 = p2.next
            else:
                ret.add_node(p1)
                p1 = p1.next
        
        while p1:
            ret.add_node(p1)
            p1 = p1.next
        
        while p2:
            ret.add_node(p2)
            p2 = p2.next
        
        return ret.head.next
        
        
        
        
        