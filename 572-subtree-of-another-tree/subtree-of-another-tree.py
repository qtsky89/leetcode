# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def is_identical(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not root and subRoot:
            return False
        elif root and not subRoot:
            return False
        elif not root and not subRoot:
            return True
        
        return root.val == subRoot.val and self.is_identical(root.left, subRoot.left) and self.is_identical(root.right, subRoot.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and subRoot:
            return False
        elif root and not subRoot:
            return False
        elif not root and not subRoot:
            return True
        
        if root.val == subRoot.val:
            if self.is_identical(root, subRoot):
                return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

