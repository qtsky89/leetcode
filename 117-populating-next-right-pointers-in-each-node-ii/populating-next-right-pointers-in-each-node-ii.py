"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        '''
        step1. ret =  [[1], [2, 3], [4, 5, 6 7]]
        
        step2. connect!
        '''

        if not root:
            return None

        # step1. ret =  [[1], [2, 3], [4, 5, 6 7]]
        ret = []
        q = deque([[root, 0]])

        while q:
            item, index = q.popleft()

            if len(ret) == index:
                ret.append([item])
            else:
                ret[index].append(item)
            
            if item.left:
                q.append([item.left, index+1])
            
            if item.right:
                q.append([item.right, index+1])
        
            # step2. connect!

            for i in range(len(ret)):
                li = ret[i]

                for j in range(len(li)-1):
                    li[j].next = li[j+1]
            
        return root





        