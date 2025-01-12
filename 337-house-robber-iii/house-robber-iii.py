# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # with_root, without_root
        def dfs(node: TreeNode) -> tuple[int, int]:
            if not node:
                return (0, 0)
            
            left_with_root, left_wihtout_root = dfs(node.left)
            right_with_root, right_without_root = dfs(node.right)

            return (left_wihtout_root+right_without_root + node.val, max(left_with_root, left_wihtout_root) + max(right_with_root, right_without_root))
        


        return max(dfs(root))