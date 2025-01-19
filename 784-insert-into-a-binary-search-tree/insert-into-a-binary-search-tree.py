# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        ret = None

        def dfs(node: TreeNode) -> None:
            if not node:
                return
            
            nonlocal ret
            ret = node
            
            if node.val < val:
                dfs(node.right)
            else:
                dfs(node.left)
        
        dfs(root)

        if val < ret.val:
            ret.left = TreeNode(val)
        else:
            ret.right = TreeNode(val)
        
        return root