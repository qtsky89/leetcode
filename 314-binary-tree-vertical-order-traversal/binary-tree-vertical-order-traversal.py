# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        whenever left, key -= 1
        whenever right, key += 1

        hash_map = {
            0 : [3]
            -1: [9, 5]
            ...
        }
        change hash_map to list
        '''

        if not root:
            return []

        hash_map = defaultdict(list)

        q = deque([[root, 0]])

        while q:
            item, key = q.popleft()

            hash_map[key].append(item.val)

            if item.left:
                q.append([item.left, key-1])
            
            if item.right:
                q.append([item.right, key+1])
        
        ret = []
        for key in sorted(hash_map.keys()):
            ret.append(hash_map[key])
        return ret
            
            

        