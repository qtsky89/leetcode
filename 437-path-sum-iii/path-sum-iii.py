# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = 0 
        def helper(root: TreeNode | None, current_sum: int):
            if not root:
                return
            nonlocal count
            current_sum += root.val

            if current_sum == targetSum:
                count += 1
            helper(root.left, current_sum)
            helper(root.right, current_sum)

        count = 0
        def dfs(node: TreeNode | None):
            if not node:
                return
            helper(node, 0)

            dfs(node.left)
            dfs(node.right)
        
        dfs(root)

        return count
