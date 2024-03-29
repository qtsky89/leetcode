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
        '''
        1 -> 2 -> 3 -> 7 -> 8  -> 11 
                    -> 4       -> 9 
        '''

        if not head:
            return None

        stack = [head]

        last = None
        while stack:
            item = stack.pop()


            if item.next:
                stack.append(item.next)

            if item.child:
                stack.append(item.child)

            if last:
                last.next = item
            item.prev = last
            item.child = None

            last = item
        
        return head


