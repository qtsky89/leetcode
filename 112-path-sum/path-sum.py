# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        ret = [False]
        def dfs(node: TreeNode, current: int):
            if not node:
                return

            current += node.val

            # leaf node
            if (not node.left) and (not node.right) and (current == targetSum):
                ret[0] = True
                return
            
            if node.left:
                dfs(node.left, current)
            
            if node.right:
                dfs(node.right, current)

        dfs(root, 0)
        
        return ret[0]
            