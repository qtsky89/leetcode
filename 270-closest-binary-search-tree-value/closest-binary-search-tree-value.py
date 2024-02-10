# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        '''
        '''

        closest = 0
        min_diff = float('inf')

        def dfs(node: TreeNode):
            if not node:
                return
            nonlocal closest
            nonlocal min_diff
            
            diff = abs(target - node.val)
            if diff < min_diff:
                closest = node.val
                min_diff = diff
            elif diff == min_diff:
                closest = min(closest, node.val)
            
            if target == node.val:
                closest = node.val
                min_diff = 0
            elif target < node.val:
                return dfs(node.left)
            elif target > node.val:
                return dfs(node.right)
        
        dfs(root)

        return closest
            