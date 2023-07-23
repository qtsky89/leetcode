# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        ret: list[list[int]] = []
        def dfs(node: TreeNode, current_sum: int, current_path: list[int]):
            if not node:
                return
            
            current_sum += node.val
            current_path.append(node.val)

            # check leaf node
            if not node.left and not node.right and current_sum == targetSum:
                ret.append(current_path)
            
            if node.left:
                dfs(node.left, current_sum, list(current_path))
            if node.right:
                dfs(node.right, current_sum, list(current_path))
                
        dfs(root, 0, [])
        
        return ret

        

