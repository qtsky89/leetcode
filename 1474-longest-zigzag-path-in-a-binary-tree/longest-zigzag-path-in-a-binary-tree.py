from enum import Enum

class Direction(Enum):
    MIDDLE = 0
    LEFT = 1
    RIGHT= 2

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        longest_length = [0]
        def dfs(node: TreeNode, prev_direction: Direction, cur_length: int):
            if not node:
                return
            
            longest_length[0] = max(longest_length[0], cur_length)

            if node.left:
                if prev_direction != Direction.LEFT:
                    dfs(node.left, Direction.LEFT, cur_length+1)
                else:
                    dfs(node.left, Direction.LEFT, 1)

            if node.right:
                if prev_direction != Direction.RIGHT:
                    dfs(node.right, Direction.RIGHT, cur_length+1)
                else:
                    dfs(node.right, Direction.RIGHT, 1)
                            
        dfs(root, Direction.MIDDLE, 0)


        return longest_length[0]
