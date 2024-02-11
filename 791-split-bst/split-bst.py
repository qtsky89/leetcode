# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        '''
                4
            2       6
        
        1      3    5   7


           2

        1
        '''

        less_euql = TreeNode(None)

        greater = TreeNode(None)

        def add(node: TreeNode, val):
            if not node:
                return
           
            if node.val == None or val < node.val:
                if node.left:
                    add(node.left, val)
                else:
                    node.left = TreeNode(val)
            elif val > node.val:
                if node.right:
                    add(node.right, val)
                else:
                    node.right = TreeNode(val)
        
        def dfs(node: TreeNode):
            if not node:
                return
            
            if node.val <= target:
                add(less_euql, node.val)
            else:
                add(greater, node.val)

            dfs(node.left)
            dfs(node.right)
        
        dfs(root)

        return [less_euql.left, greater.left]