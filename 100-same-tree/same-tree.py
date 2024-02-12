# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        using recurse, dfs function, 

        every step, we can check the value is same 
            1. value it self should be same
            2. type should be same like None
        '''

        # breaking point
        if not p and q:
            return False
        elif p and not q:
            return False
        elif not q and not q:
            return True
        
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)