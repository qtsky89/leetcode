class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        '''
        obstacleGrid = [0,1,0]   dp = 1 0 0
                       [0,0,0]        1 1 1
                       [0,0,0]        1 2 3


        '''

        dp = [[0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]

        for i in range(len(obstacleGrid)):
            # obstacle
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1
        
        for j in range(len(obstacleGrid[0])):
            if obstacleGrid[0][j] == 1:
                break
            
            dp[0][j] = 1
        

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        print(dp)
        
        return dp[-1][-1]