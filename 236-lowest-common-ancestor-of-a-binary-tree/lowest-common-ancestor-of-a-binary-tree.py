# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        parent_map = {
            5 : 3
            6 : 5 
        }
        '''

        parent_map = {root: None}
        def dfs(node: TreeNode):
            if not root:
                return
            
            if node.left:
                parent_map[node.left] = node
                dfs(node.left)
            
            if node.right:
                parent_map[node.right] = node
                dfs(node.right)

        dfs(root)

        visited = set()
        i = p
        while i:
            visited.add(i)
            i = parent_map[i]

        i = q
        while i:
            if i in visited:
                return i
            i = parent_map[i]


