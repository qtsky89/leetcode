"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque, defaultdict

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        hash_table = defaultdict(list)
        
        q = deque([[root, 0]])
        while q:
            node, level = q.popleft()
            
            hash_table[level].append(node)
            
            if node.left:
                q.append([node.left, level+1])
            
            if node.right:
                q.append([node.right, level+1])
        
        for tmp in hash_table.values():
            for i in range(len(tmp)-1):
                tmp[i].next = tmp[i+1]
        
        return root
        
        
        
        
            
            
            
        
        
        