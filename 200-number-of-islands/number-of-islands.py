class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # turn to adjacent ground to water
        def dfs(i: int, j: int) -> None:
            grid[i][j] = '0'

            # south
            if (i+1) <= len(grid)-1 and grid[i+1][j] == '1':
                dfs(i+1, j)
            # east
            if (j+1) <= len(grid[0])-1 and grid[i][j+1] == '1':
                dfs(i, j+1)
            # north
            if (i-1) >= 0  and grid[i-1][j] == '1':
                dfs(i-1, j)
            # west
            if (j-1) >= 0 and grid[i][j-1] == '1':
                dfs(i, j-1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count