# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        example1.

                 3
                
            5(p)     1(q)
             |
          6   2    0    8
               |
            7   4

        step1. make these hash function
        {  
            4 : 2
            2 : 5
            5 : 3
        }

        step2. make these list
        4 -> 2 -> 5V -> 3
        5V -> 3

        step3. find common anccestor
        '''

        # step1
        hash_map = {}

        def dfs(node: TreeNode):
            if not node:
                return
            
            if node.left:
                hash_map[node.left] = node
                dfs(node.left)
            if node.right:
                hash_map[node.right] = node
                dfs(node.right)
        
        hash_map[root] = None
        dfs(root)

        #step2. make these list

        visited = set()

        while p:
            if p in visited:
                return p
            visited.add(p)
            p = hash_map[p]
        
        while q:
            if q in visited:
                return q
            visited.add(q)
            q = hash_map[q]
        return None
