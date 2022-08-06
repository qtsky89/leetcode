class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i: int, j: int, count: List[int]):
            grid[i][j] = 0
            
            count[0] += 1
            
            if i+1 <= len(grid)-1 and grid[i+1][j] ==1:
                dfs(i+1, j, count)
            
            if i-1 >= 0 and grid[i-1][j] == 1:
                dfs(i-1, j, count)
            
            if j+1 <= len(grid[0])-1 and grid[i][j+1] == 1:
                dfs(i, j+1, count)
            
            if j-1 >= 0 and grid[i][j-1] == 1:
                dfs(i, j-1, count)
        
        
        max_length = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                count = [0]
                if grid[i][j] == 1:
                    dfs(i, j, count)
                
                max_length = max(max_length, count[0])
        return max_length
                