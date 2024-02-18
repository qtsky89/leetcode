# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
        inorder
        '''

        count = 0
        ret = 0
        def dfs(node: TreeNode):
            if not node:
                return
            
            dfs(node.left)

            nonlocal count
            count += 1

            if count == k:
                nonlocal ret
                ret = node.val

            dfs(node.right)
            

        dfs(root)
        return ret