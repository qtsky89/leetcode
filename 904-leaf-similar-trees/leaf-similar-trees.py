# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        '''
        1. I have to implement dfs function
        2. using dfs both of trees, and make leaf array
        3. compare those leaf array
        4. it's same return True, else False
        '''

        # 1. I have to implement dfs function
        def dfs(node: TreeNode, leaf_arr: list[int]):
            if not node:
                return

            # leaf
            if not node.left and not node.right:
                leaf_arr.append(node.val)
            
            dfs(node.left, leaf_arr)
            dfs(node.right, leaf_arr)
        
        leaf_arr1, leaf_arr2 = [], []

        dfs(root1, leaf_arr1)
        dfs(root2, leaf_arr2)

        return leaf_arr1 == leaf_arr2

