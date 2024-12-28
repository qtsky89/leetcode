# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def is_identical(node1: TreeNode, node2: TreeNode) -> bool:
    if not node1 and not node2:
        return True
    elif not (node1 and node2):
        return False
    elif node1.val != node2.val:
        return False
    
    return is_identical(node1.left, node2.left) and is_identical(node1.right, node2.right)


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:           
        if not root:
            return False

        if (root and subRoot) and root.val == subRoot.val and is_identical(root, subRoot):
            return True
            
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
