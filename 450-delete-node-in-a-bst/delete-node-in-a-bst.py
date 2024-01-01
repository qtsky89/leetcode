# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def _next_min_val(self, node: TreeNode) -> int:
        p = node
        while p.left:
            p = p.left
        return p.val
    
    def _previous_max_val(self, node: TreeNode) -> int:
        p = node
        while p.right:
            p = p.right
        return p.val

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else: # key = root.val
            # leaf
            if not root.left and not root.right:
                root = None
            elif root.left:
                root.val = self._previous_max_val(root.left)
                root.left = self.deleteNode(root.left, root.val)
            else:
                root.val = self._next_min_val(root.right)
                root.right = self.deleteNode(root.right, root.val)
        return root

        