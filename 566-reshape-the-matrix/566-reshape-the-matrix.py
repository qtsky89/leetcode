class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if not mat:
            return mat
        
        if len(mat) * len(mat[0]) != r*c:
            return mat
        
        ret: List[List[int]] = [[0 for __ in range(c)] for _ in range(r)]
        x, y = 0, 0
        
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                tmp = mat[i][j]
                
                ret[x][y] = tmp
                
                y += 1
                
                if y >= c:
                    y = 0
                    x += 1
        return ret
                    
                
        
        
        
        