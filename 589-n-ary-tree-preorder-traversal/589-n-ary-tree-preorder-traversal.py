"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ret = []
        
        
        def dfs(node: 'Node'):
            if not node:
                return
            
            ret.append(node.val)
            
            for c in node.children:
                dfs(c)
            
        dfs(root)
        
        return ret