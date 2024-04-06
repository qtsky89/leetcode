class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        def dfs(first_i: int, first_j: int, i: int, j: int, shape: list[str]) -> None:
            # make it water
            grid[i][j] = 0

            if i+1 <= len(grid)-1 and grid[i+1][j] == 1:
                shape.append('D')
                dfs(first_i, first_j, i+1, j, shape)
            if j+1 <= len(grid[0])-1 and grid[i][j+1] == 1:
                shape.append('R')
                dfs(first_i, first_j, i, j+1, shape)
            if i-1 >= 0 and grid[i-1][j] == 1:
                shape.append('U')
                dfs(first_i, first_j, i-1, j, shape)
            if j-1 >= 0 and grid[i][j-1] == 1:
                shape.append('L')
                dfs(first_i, first_j, i, j-1, shape)
            shape.append('X')
            
        shapes = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    shape = ['N']
                    dfs(i, j, i, j, shape)
                    shapes.add(''.join(shape))

        return len(shapes)