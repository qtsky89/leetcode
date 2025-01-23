class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        '''
        dp => 2d array

        dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        '''

        dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        for i in range(len(grid)):
            dp[i][0] = grid[i][0] + (dp[i-1][0] if i-1 >= 0 else 0)
        
        for j in range(len(grid[0])):
            dp[0][j] = grid[0][j] + (dp[0][j-1] if j-1 >= 0 else 0)
        
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        
        return dp[-1][-1]