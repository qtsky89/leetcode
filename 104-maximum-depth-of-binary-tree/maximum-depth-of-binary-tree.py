# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
            3          
        9      20
            15     7

        max_depth = 0
        '''
        if not root:
            return 0

        max_depth = 0
        def dfs(node: TreeNode, current_depth: int):
            if not node:
                return
            
            nonlocal max_depth

            max_depth = max(max_depth, current_depth)

            dfs(node.left, current_depth+1)
            dfs(node.right, current_depth+1)
        
        dfs(root, 1)

        return max_depth