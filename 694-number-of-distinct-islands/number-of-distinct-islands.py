class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        '''
        N R L U D
        '''

        def dfs(i: int, j: int, current_work: list[str]) -> None:
            # don't want to visit again
            grid[i][j] = 0

            if i + 1 <= len(grid)-1 and grid[i+1][j] == 1:
                current_work.append('D')
                dfs(i+1, j, current_work)
            
            if i - 1 >= 0 and grid[i-1][j] == 1:
                current_work.append('U')
                dfs(i-1, j, current_work)
            
            if j + 1 <= len(grid[0]) -1 and grid[i][j+1] == 1:
                current_work.append('R')
                dfs(i, j+1, current_work)
            
            if j - 1 >= 0 and grid[i][j-1] == 1:
                current_work.append('L')
                dfs(i, j-1, current_work)
            
            current_work.append('Z')

        ret: set[str] = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    current_work = ['N']
                    dfs(i, j, current_work)
                    ret.add(''.join(current_work))
        
        return len(ret)