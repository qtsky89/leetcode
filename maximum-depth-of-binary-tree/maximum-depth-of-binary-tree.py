# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        
        max_depth = [1]

        def recursive(node: TreeNode, current_depth: int):
            max_depth[0] = max(max_depth[0], current_depth)
            
            if node.left:
                recursive(node.left, current_depth+1)
            
            if node.right:
                recursive(node.right, current_depth+1)
        

        recursive(root, 1)

        return max_depth[0]