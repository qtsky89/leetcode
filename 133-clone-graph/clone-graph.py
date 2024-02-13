"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional

from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_new: dict[Node, Node] = {}
        
        def dfs(n: node) -> node:
            if n in old_new:
                return old_new[n]
            
            copy = Node(n.val)
            old_new[n] = copy

            for neighbor in n.neighbors:
                copy.neighbors.append(dfs(neighbor))
            
            return copy
            

        return dfs(node) if node else None
            

        



        