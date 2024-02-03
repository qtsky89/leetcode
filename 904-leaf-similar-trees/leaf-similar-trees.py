# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        '''
            3
        5       1
      6  2     9  8
      
        7  4

        def leaf node:  there is no child node


        step 1. preorder travel each tree
        step 2. if leaf add to list
        step 3. compare two list
        '''

        def dfs(node: TreeNode, leafs: list[int]):
            if not node:
                return

            # if it's leaf
            if not node.left and not node.right:
                leafs.append(node.val)
            
            dfs(node.left, leafs)
            dfs(node.right, leafs)

        leafs1: list[int] = []
        leafs2: list[int] = []

        dfs(root1, leafs1)
        dfs(root2, leafs2)

        return leafs1 == leafs2
        