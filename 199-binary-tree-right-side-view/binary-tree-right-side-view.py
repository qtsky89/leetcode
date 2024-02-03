# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
          1          <-1
        2   3        <-3

          5     4    <-4

        [ [1] , [2, 3], [5, 4] ]

            1, 3, 4
        '''

        if not root:
            return None

        q = deque([[root, 0]])

        tmp = []
        '''
        [ [1], [2, 3], [5, 4] ] => [1, 3, 4]
        '''
        while q:
            item, level = q.popleft()

            if level == len(tmp):
                tmp.append(item.val)
            else:
                tmp[level] = item.val
            
            if item.left:
                q.append([item.left, level+1])
            if item.right:
                q.append([item.right, level+1])
        
        return tmp
        
        
        

        
            
            
                
            
        
