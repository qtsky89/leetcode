"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def __init__(self) -> None:
        self._old_new: dict[Node, Node] = {}

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        if node not in self._old_new:
            new_node = Node(node.val)

            self._old_new[node] = new_node
            
            for neighbor in node.neighbors:
                new_node.neighbors.append(self.cloneGraph(neighbor))

        return self._old_new[node]