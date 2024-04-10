class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        def dfs(i: int, j: int, current_area: list[int]) -> None:
            nonlocal max_area
            grid[i][j] = 0

            max_area = max(max_area, current_area[0])

            if i + 1 <= len(grid)-1 and grid[i+1][j] == 1:
                current_area[0] += 1
                dfs(i+1, j, current_area)
            
            if i - 1 >= 0 and grid[i-1][j] == 1:
                current_area[0] += 1
                dfs(i-1, j, current_area)
            
            if j + 1 <= len(grid[0])-1 and grid[i][j+1] == 1:
                current_area[0] += 1
                dfs(i, j+1, current_area)
            
            if j - 1 >= 0 and grid[i][j-1] == 1:
                current_area[0] += 1
                dfs(i, j-1, current_area)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(i, j, [1])
        
        return max_area