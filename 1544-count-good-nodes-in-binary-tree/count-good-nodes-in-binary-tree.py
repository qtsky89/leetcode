# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(node: TreeNode, max_value: int) -> None:
            if not node:
                return

            if node.val >= max_value:
                nonlocal count
                count += 1
                max_value = max(max_value, node.val)
            
            dfs(node.left, max_value)
            dfs(node.right, max_value)

        dfs(root, -float('inf'))

        return count