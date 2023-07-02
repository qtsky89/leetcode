# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        elif not (root1 and root2):
            return False

        r1 = self._get_leafs(root1)
        r2 = self._get_leafs(root2)

        print(r1)
        print(r2)

        return r1 == r2

    def _get_leafs(self, node: TreeNode) -> list[int]:
        ret: list[int] = []        
        def dfs(node: TreeNode):
            if node.left:
                dfs(node.left)
            
            if not node.left and not node.right:
                ret.append(node.val)
            
            if node.right:
                dfs(node.right)
        
        dfs(node)

        return ret