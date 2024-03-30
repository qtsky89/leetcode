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
        '''
        7 -> 13 -> 11 -> 10 -> 1

        7 -> 7' -> 13 -> 13' -> 11 -> 11' -> 10 -> 10' -> 1 -> 1'
        '''

        if not head:
            return None

        p = head

        while p:
            tmp = p.next
            node = Node(p.val)
            p.next = node
            node.next = tmp
            p = tmp
        '''
        7 -> 7' -> 13 -> 13' -> 11 -> 11' -> 10 -> 10' -> 1 -> 1'
        '''
        p = head
        while p and p.next:
            p.next.random = p.random.next if p.random else None
            p = p.next.next
        
        p = head.next
        while p and p.next:
            p.next = p.next.next
            p = p.next
        
        return head.next


