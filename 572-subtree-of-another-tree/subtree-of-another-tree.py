# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def is_identical(self, node1: TreeNode, node2: TreeNode) -> bool:
        ret = True

        def dfs(node1: TreeNode, node2: TreeNode) -> None:
            nonlocal ret
            if node1 and not node2:
                ret = False
                return
            elif not node1 and node2:
                ret = False
                return
            elif not node1 and not node2:
                return
            elif node1.val != node2.val:
                ret = False
                return
            
            dfs(node1.left, node2.left)
            dfs(node1.right, node2.right)
        
        dfs(node1, node2)

        return ret


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # find target first
        ret = False
        def dfs(node: TreeNode) -> None:
            if not node:
                return None
            
            if node.val == subRoot.val and self.is_identical(node, subRoot):
                nonlocal ret
                ret = True
                return
            
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)

        return ret



        