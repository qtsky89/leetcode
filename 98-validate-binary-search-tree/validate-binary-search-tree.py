# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: TreeNode, min_value: int, max_value: int):
            if not node:
                return True
            
            if not(min_value < node.val < max_value):
                return False
            
            return dfs(node.left, min_value, node.val) and dfs(node.right, node.val, max_value)
                
        
        return dfs(root, -float('inf'), float('inf'))