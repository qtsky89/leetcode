# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
        BST using inOrder approach

                    3
                1        4

             => V1 -> V3 -> V4
        '''
        
        ret = -float('inf')

        count = 0
        def dfs(node: TreeNode | None):
            nonlocal ret
            if not node or ret != -float('inf'):
                return None
        
            dfs(node.left)
            
            nonlocal count
            count += 1

            if count == k:
                ret = node.val

            dfs(node.right)
        

        dfs(root)

        return ret


