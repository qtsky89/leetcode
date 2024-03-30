# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ret = True
        def dfs(node: TreeNode, min_val: int, max_val: int):
            nonlocal ret
            if not node or not ret:
                return
            
            if not(min_val < node.val < max_val):
                ret = False
            
            dfs(node.left, min_val, node.val)
            dfs(node.right, node.val, max_val)

        dfs(root, -float('inf'), float('inf'))

        return ret

        