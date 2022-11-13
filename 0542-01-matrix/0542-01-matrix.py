from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        
        q = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append([i, j, 0])
        
        # q = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 2], [2, 0], [2, 1], [2, 2]]
        
        ret = [[-1 for __ in range(n)] for _ in range(m)]
        
        while q:
            i, j, count = q.popleft()
            
            if ret[i][j] != -1 and ret[i][j] < count:
                continue
            
            ret[i][j] = count
            
            if i + 1 <= m - 1 and mat[i+1][j] == 1:
                q.append([i+1, j, count+1])
            
            if j + 1 <= n - 1 and mat[i][j+1] == 1:
                q.append([i, j+1, count+1])
            
            if i - 1 >= 0 and mat[i-1][j] == 1:
                q.append([i-1, j, count+1])
            
            if j - 1 >= 0 and mat[i][j-1] == 1:
                q.append([i, j-1, count+1])
            
        return ret
            
        
            
            
            
            
                    
        