# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ret = True
        # height
        def height(node: TreeNode) -> int:
            if not node:
                return 0

            left, right = height(node.left), height(node.right)

            if abs(left-right) > 1:
                nonlocal ret
                ret = False

            return max(left, right) + 1
        
        height(root)

        return ret

