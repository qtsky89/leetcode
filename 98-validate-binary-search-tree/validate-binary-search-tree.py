# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        ret = True
        def isValid(node: TreeNode, min_value: int, max_value: int) -> None:
            if not node:
                return
            
            if not (min_value < node.val < max_value):
                nonlocal ret
                ret = False
            
            isValid(node.left, min_value, node.val)
            isValid(node.right, node.val, max_value)
            
        isValid(root, -float('inf'), float('inf'))

        return ret
        
