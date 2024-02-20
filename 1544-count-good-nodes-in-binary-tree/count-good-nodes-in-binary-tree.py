# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        '''
        1. make dfs function to travel. but keep the maximum value of the path
        2. if current_node value is bigger or same the maximum value count += 1
        3. return count
        '''

        if not root:
            return 0


        count = 0
        def dfs(node: TreeNode, maximum_value: int):
            if not node:
                return
            
            # 2. if current_node value is bigger or same the maximum value count += 1
            if node.val >= maximum_value:
                nonlocal count
                count += 1
            
            dfs(node.left, max(node.val, maximum_value))
            dfs(node.right, max(node.val, maximum_value))

        dfs(root, root.val)

        return count
