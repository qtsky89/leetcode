class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        '''
        closed island
        0 land

        1 water

        1. nested for loop, if i found 0 then use dfs, make it 1, 
        2. when we do that, check if surrounded or not. if not surrounded mark that but don't count
        '''

        def dfs(i: int, j: int):
            if grid[i][j] == 1:
                return

            grid[i][j] = 1

            if i+1 <= len(grid)-1 and grid[i+1][j] == 0:
                dfs(i+1, j)
            
            if j+1 <= len(grid[0])-1  and grid[i][j+1] == 0:
                dfs(i, j+1)
            
            if i-1 >= 0  and grid[i-1][j] == 0:
                dfs(i-1, j)
            
            if j-1 >= 0  and grid[i][j-1] == 0:
                dfs(i, j-1)

        for i in range(len(grid)):
            dfs(i, 0)
            dfs(i, len(grid[0])-1)
        
        for j in range(len(grid[0])):
            dfs(0, j)
            dfs(len(grid)-1, j)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    dfs(i, j)
                    count += 1

        return count