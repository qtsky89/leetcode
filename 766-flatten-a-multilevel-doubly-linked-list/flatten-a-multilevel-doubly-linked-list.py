"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        stack = [head]

        last = None
        while stack:
            item = stack.pop()

            if last:
                last.next, item.prev = item, last
            last = item

            if item.next:
                stack.append(item.next)

            if item.child:
                stack.append(item.child)
            item.child = None
        
        return head
            



            
            
        





