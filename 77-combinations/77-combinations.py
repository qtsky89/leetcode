from collections import deque

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # q = [[1],[2],[3],[4]]
        q = deque([[i] for i in range(1, n+1)])
        
        ret = []
        while q:
            # [1]
            item = q.popleft()
            
            if len(item) == k:
                ret.append(item)
                continue
            
            for i in range(item[-1]+1, n+1):
                q.append(item + [i])
        
        return ret
            
        
        