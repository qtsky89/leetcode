# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # key: child, value: parent
        parent_map: dict[TreeNode, TreeNode] = {}

        def dfs(node: TreeNode | None) -> None:
            if not node:
                return
            
            if node.left:
                parent_map[node.left] = node
                dfs(node.left)
            if node.right:
                parent_map[node.right] = node
                dfs(node.right)

        parent_map[root] = None
        dfs(root)

        visited = set()
        while p and q:
            if p == q:
                return p
            elif p in visited:
                return p
            elif q in visited:
                return q

            visited.add(p)
            visited.add(q)

            if p in parent_map:
                p = parent_map[p]
            else:
                p = None
            if q in parent_map:
                q = parent_map[q]
            else:
                q = None
        
        while p:
            if p in visited:
                return p
            else:
                visited.add(p)

            if p in parent_map:
                p = parent_map[p]
            else:
                p = None

        while q:
            if q in visited:
                return q
            else:
                visited.add(q)

            if q in parent_map:
                q = parent_map[q]
            else:
                q = None