# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        ret = False
        def dfs(node: TreeNode, current_sum: int):
            if not node:
                return

            tmp = current_sum + node.val
            # need to be leaf
            if not node.left and not node.right and tmp == targetSum:
                nonlocal ret
                ret = True
            
            dfs(node.left, tmp)
            dfs(node.right, tmp)

        dfs(root, 0)

        return ret