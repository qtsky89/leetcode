# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        '''
            1
              1
            1   1
               1   1
                 1
                   1

            if previous action is right:
                we can continue with left child
                we can continue with right child with 0 count
            else 
                we can continue with right child
                we can continue with left child with 0 count
            
            return max count
        ''' 

        max_count = 0

        # current_path => L, R, None(init)
        def dfs(node: TreeNode, current_path: str | None , current_count):
            if not node:
                return
            
            nonlocal max_count

            max_count = max(max_count, current_count)

            if current_path is None:
                dfs(node.left, 'L', 1)
                dfs(node.right, 'R', 1)
            elif current_path == 'R':
                dfs(node.left, 'L', current_count + 1)
                dfs(node.right, 'R', 1)
            else:
                dfs(node.left, 'L', 1)
                dfs(node.right, 'R', current_count + 1)
            
        dfs(root, None, 0)

        return max_count