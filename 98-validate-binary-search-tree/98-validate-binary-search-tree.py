# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(node: TreeNode, low: int, high: int)-> bool:
            if not node:
                return True
            
            if not (low < node.val < high):
                return False
            
            left_validate = validate(node.left, low, node.val) if node.left else True
            right_validate = validate(node.right, node.val, high) if node.right else True
            
            return left_validate and right_validate
            
        return validate(root, -float('inf'), float('inf'))