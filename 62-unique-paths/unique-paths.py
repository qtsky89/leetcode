class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        1 1 1 1 1 1 1 1
        1 2 * * * * * *
        1 * * * * * * *

        
        dp[0][~] = 1
        dp[~][0] = 1
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
        '''

        dp = [[0 for j in range(n)]  for i in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for i in range(n):
            dp[0][i] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[-1][-1]

        