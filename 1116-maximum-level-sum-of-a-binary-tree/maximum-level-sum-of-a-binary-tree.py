# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        '''
            1       -> 1
        7       0   -> 7
    7       -8      -> -1
        '''

        ret = []
        q = deque([[root, 0]])

        while q:
            item, level = q.popleft()

            if level == len(ret):
                ret.append(item.val)
            else:
                ret[level] += item.val
            
            if item.left:
                q.append([item.left, level+1])
            if item.right:
                q.append([item.right, level+1])

        max_val = -float('inf')

        ret_i = 0

        for i in range(len(ret)):
            if ret[i] > max_val:
                ret_i = i
                max_val = ret[i]
        return ret_i+1
