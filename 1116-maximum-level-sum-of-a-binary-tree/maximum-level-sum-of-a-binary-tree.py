# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        q = deque([[root, 1]])

        # 1 : 1, 2: 7, 3: -1
        hash_map = {}
        while q:
            item, cur_level = q.popleft()

            if cur_level in hash_map:
                hash_map[cur_level] += item.val
            else:
                hash_map[cur_level] = item.val

            if item.left:
                q.append([item.left, cur_level+1])
            if item.right:
                q.append([item.right, cur_level+1])
        
        
        max_val = -float('inf')
        max_level = 1
        for k in hash_map:
            if max_val < hash_map[k]:
                max_val = hash_map[k]
                max_level = k
            
        
        return max_level

            
        