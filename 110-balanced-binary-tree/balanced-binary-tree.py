# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        '''
        every node can evaluate left right height 

        the differ is more than one => return False
        '''

        ret = True

        def height(node: TreeNode) -> int:
            if not node:
                return 0
            
            left_height = height(node.left)
            right_height = height(node.right)

            if abs(left_height - right_height) > 1:
                nonlocal ret
                ret = False
                return 0
            
            return max(left_height, right_height) + 1
            
        height(root)

        return ret