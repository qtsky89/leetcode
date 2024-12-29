# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        longest_diameter = 0

        # left height + right height => longest_diameter
        def height(node: TreeNode)-> int:
            if not node:
                return 0

            left, right = height(node.left), height(node.right)
            nonlocal longest_diameter
            longest_diameter = max(longest_diameter, left + right)

            return max(left, right) + 1
        
        height(root)

        return longest_diameter
            