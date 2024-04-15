class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        count = 0        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    c = 4

                    if i+1 <= len(grid)-1 and grid[i+1][j] == 1:
                        c -=1
                    if i-1 >= 0 and grid[i-1][j] == 1:
                        c -=1
                    if j+1 <= len(grid[0])-1 and grid[i][j+1] == 1:
                        c -= 1
                    if j-1 >= 0 and grid[i][j-1] == 1:
                        c -= 1
                    count += c
        return count
        