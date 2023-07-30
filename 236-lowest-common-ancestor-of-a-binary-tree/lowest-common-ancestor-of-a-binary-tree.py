# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        '''
      key   value(parent)
       3 -> None
       5 -> 3
       ...
        '''

        # key: TreeNode, value: TreeNode(parent)
        parent_map = {}

        def dfs(node: TreeNode | None):
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
        while p:
            if p in visited:
                return p
            visited.add(p)
            p = parent_map[p]
        
        while q:
            if q in visited:
                return q
            visited.add(q)
            q = parent_map[q]
        
        return None