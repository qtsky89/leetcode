# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
           1
          2 3
         5 4 

         ret = [[1], [2, 3], [5, 4]]

         [1, 3, 4]
        '''

        if not root:
            return []

        q = deque([[root, 0]])

        ret = []
        while q:
            item, index = q.popleft()

            if index == len(ret):
                ret.append([item.val])
            else:
                ret[index].append(item.val)
            
            if item.left:
                q.append([item.left, index+1])
            if item.right:
                q.append([item.right, index+1])
        
        filtered_ret = []
        for li in ret:
            filtered_ret.append(li[-1])
        
        return filtered_ret
        
