# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ret = 0

        def dfs(node: TreeNode, max_val: int) -> None:
            if not node:
                return

            nonlocal ret
            if max_val <= node.val:
                ret += 1
                max_val = node.val
            
            dfs(node.left, max_val)
            dfs(node.right, max_val)
            
        dfs(root, -float('inf'))

        return ret