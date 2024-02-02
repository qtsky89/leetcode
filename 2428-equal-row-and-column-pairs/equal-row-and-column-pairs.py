class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        '''
        11 1
        1 11


        visited = {'321', '176', '277'}       
        '''

        row_count = {}
        for li in grid:
            key = tuple(li)

            if key in row_count:
                row_count[key] += 1
            else:
                row_count[key] = 1
        
        
        col_count = {}
        for j in range(len(grid[0])):
            tmp = []
            for i in range(len(grid)):
                tmp.append(grid[i][j])
            
            key = tuple(tmp)
            if key in col_count:
                col_count[key] += 1
            else:
                col_count[key] = 1

        count = 0
        for key in row_count:
            if key in col_count:
                count += row_count[key] * col_count[key]
        return count