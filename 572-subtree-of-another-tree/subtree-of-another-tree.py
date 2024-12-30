# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def is_identical(node1: TreeNode, node2: TreeNode) -> bool:
    if not node1 and not node2:
        return True
    
    if not(node1 and node2):
        return False
        
    return node1.val == node2.val and is_identical(node1.left, node2.left) and is_identical(node1.right, node2.right)


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        ret = False
        def dfs(node: TreeNode) -> None:
            if not node:
                return
            
            if node.val == subRoot.val and is_identical(node, subRoot):
                nonlocal ret
                ret = True
                return
            
            dfs(node.left)
            dfs(node.right)

            
        dfs(root)

        
        return ret
        