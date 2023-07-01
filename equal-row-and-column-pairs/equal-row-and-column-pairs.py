class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        '''
        3  2  1 
        1  7  6
        2  7  7
        '''

        n = len(grid)
        row, col = [], []

        for i in range(n):
            tmp = []
            for j in range(n):
                tmp.append(str(grid[i][j]))
            
            tmp_str = ','.join(tmp)
            row.append(tmp_str)
        
        for j in range(n):
            tmp = []
            for i in range(n):
                tmp.append(str(grid[i][j]))
            
            tmp_str = ','.join(tmp)
            col.append(tmp_str)
        
        count = 0
        for r in row:
            for c in col:
                if r == c:
                    count += 1

        
        return count

