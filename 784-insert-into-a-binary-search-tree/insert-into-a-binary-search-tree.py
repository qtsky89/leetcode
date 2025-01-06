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
        
        last_node = None
        def dfs(node: TreeNode) -> None:
            if not node:
                return

            nonlocal last_node            
            last_node = node

            if val < node.val:
                dfs(node.left)
            else:
                dfs(node.right)

        dfs(root)

        if val < last_node.val:
            last_node.left = TreeNode(val)
        else:
            last_node.right = TreeNode(val)
        
        return root