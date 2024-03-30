class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        '''
        1  0  0              7 0 0    
       -1  0  3              0 0 0        mat1[0][0] * mat2[0][0] + mat1[0][0] * mat2[1][0] + mat1[0][0] * mat2[2][0]
                             0 0 1        mat1[1][0] * mat2[0][0] + mat1[1][1] * mat2[1][0] + mat1[1][2] * mat2[2][0]
        
        2 * 3                 3 * 3        2 * 3
        '''
        
        # find m, n, k
        m, n, k = len(mat1), len(mat1[0]), len(mat2[0])

        ret = [[0 for __ in range(k)] for _ in range(m)]

        for i in range(m):
            for j in range(k):
                tmp = 0
                
                for x in range(n):
                    tmp += mat1[i][x] * mat2[x][j]
                
                ret[i][j] = tmp
        
        return ret
        