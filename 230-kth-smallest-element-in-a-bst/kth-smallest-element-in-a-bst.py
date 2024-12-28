# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        index = 0
        smallest = 0

        def inorder(node: TreeNode) -> None:
            if not node:
                return
            
            inorder(node.left)
            
            nonlocal index
            nonlocal smallest
            index += 1
            if index == k:
                smallest = node.val
            
            inorder(node.right)

        inorder(root)

        return smallest