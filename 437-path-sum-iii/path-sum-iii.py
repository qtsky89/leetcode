# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], target_sum: int) -> int:
        '''
                 10

              5      -3

            3     2      11

          3  -2      1

        step1. preorder 
        step2. every node, I 'm going to pre order again keep sum and when targetSum is same then, increase count
        step3. return count
        '''

        count = 0

        def dfs_sum(node: TreeNode, current_sum: int):
            if not node:
                return

            nonlocal count

            current_sum += node.val
            if current_sum == target_sum:
                count += 1
            
            dfs_sum(node.left, current_sum)
            dfs_sum(node.right, current_sum)

        def dfs(node: TreeNode):
            if not node:
                return
            
            dfs_sum(node, 0)

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return count