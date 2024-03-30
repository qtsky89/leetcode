"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return

        ret = []

        q = deque([[root, 0]])
        while q:
            item, index = q.popleft()

            if len(ret) == index:
                ret.append([item])
            else:
                ret[index].append(item)
            
            if item.left:
                q.append([item.left, index+1])
            if item.right:
                q.append([item.right, index+1])

        for i in range(len(ret)):
            for j in range(len(ret[i])-1):
                ret[i][j].next = ret[i][j+1]
        
        return root

        