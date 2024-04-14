"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None
        '''
        step1 make this
        7 -> 7` -> 13 -> 13` -> 11 -> 11` -> 10 -> 10` -> 1 -> 1`-> None

        step2.copy random pointer

        '''
        # step1 make this
        # 7 -> 7` -> 13 -> 13` -> 11 -> 11` -> 10 -> 10` -> 1 -> 1`-> None

        p = head
        while p:
            next_node = p.next
            tmp = Node(p.val)

            p.next = tmp
            tmp.next = next_node

            p = next_node

        # step2. copy random pointer
        p = head
        while p and p.next:
            p.next.random = p.random.next if p.random else None
            p = p.next.next

        new_head = head.next
        p = new_head
        while p and p.next:
            p.next = p.next.next
            p = p.next
        
        return new_head

            
            

        