class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        '''
        triangle = 
        2
        3 4
        6 5 7
        4 1 8 3
        '''
        
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j==0:
                    triangle[i][j] += triangle[i-1][j]
                elif 1 <= j < len(triangle[i])-1:
                    triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
                else:
                    triangle[i][j] += triangle[i-1][j-1]
        
        
        print(triangle)
        
        return min(triangle[-1])
        
        