# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        '''
                3

            1        4
        
        3            1     5


        preorder : 3 -> 1 -> 3 -> 4 -> 1 -> 5
                                       ^
                                    3 -> 4 -> 1
        we need to keep max node val through path.

        if node.val >= max_val:
            count += 1
        '''

        count = 0

        def dfs(node: TreeNode, max_val):
            if not node:
                return
            
            nonlocal count
            if node.val >= max_val:
                count += 1

            max_val = max(max_val, node.val)

            dfs(node.left, max_val)
            dfs(node.right, max_val)
        
        dfs(root, -float('inf'))
        
        return count