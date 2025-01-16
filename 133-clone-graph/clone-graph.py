"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, root: Optional['Node']) -> Optional['Node']:
        '''
        {
            old_node : new_node...
        }
        '''

        cache: dict[Node, Node] = {}
        
        def dfs(node: Node) -> None:
            if not node:
                return

            if node not in cache:
                new_node = Node(node.val)
                cache[node] = new_node

                for neighbor in node.neighbors:
                    new_node.neighbors.append(dfs(neighbor))

            return cache[node]
        
        return dfs(root)






