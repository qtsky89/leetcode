# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_node_counts = [0]

        def dfs(node: TreeNode, max_val: int):
            if node.val >= max_val:
                good_node_counts[0] +=1
            
            new_max_val = max(max_val, node.val)
            
            if node.left:
                dfs(node.left, new_max_val)
            
            if node.right:
                dfs(node.right, new_max_val)
            
            
        dfs(root, -float('inf'))

        return good_node_counts[0]