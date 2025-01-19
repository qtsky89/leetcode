# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:


        # (node_included_max, node_not_included_max)
        def dfs(node: TreeNode) -> tuple[int, int]:
            if not node:
                return (0, 0)
            
            left_included_max, left_not_included_max = dfs(node.left)
            right_included_max, right_not_included_max  = dfs(node.right)

            
            return (node.val + left_not_included_max + right_not_included_max, max(left_included_max, left_not_included_max) + max(right_included_max, right_not_included_max))
        

        return max(dfs(root))