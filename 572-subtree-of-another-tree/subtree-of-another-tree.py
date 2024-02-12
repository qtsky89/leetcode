# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        '''
        1. let's find subRoot in root
        2. if I coulnd't find the subRoot then reutrn False
        3. if I could find that subRoot, check it's childrens are all same
        '''

        def dfs(node: TreeNode) -> bool:
            if not node:
                return False
            
            return isSame(node, subRoot) or dfs(node.left) or dfs(node.right)

        # if there is subRoot's value in root
        def isSame(node: TreeNode, sub_node: TreeNode) -> bool:
            if node and not sub_node:
                return False
            elif not node and sub_node:
                return False
            elif not node and not sub_node:
                return True
            
            return node.val == sub_node.val and isSame(node.left, sub_node.left) and isSame(node.right, sub_node.right)

            
        return dfs(root)