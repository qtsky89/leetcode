# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def biggestNode(self, node: TreeNode) -> TreeNode:
        p = node
        while p and p.right:
            p = p.right
        return p


    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.val == key:
            # leaf
            if not root.left and not root.right:
                return None
            elif not root.left:
                return root.right
            elif not root.right:
                return root.left
            else: # two children is alive
                node = self.biggestNode(root.left)
                root.val = node.val
                root.left = self.deleteNode(root.left, node.val)

        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)

        return root
        
