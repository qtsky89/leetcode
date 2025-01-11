class Solution:
    def numSquares(self, n: int) -> int:
        '''
        n = dp[82] => dp[81] + dp[1]

                   dp[83] = dp[81] + dp[2]
                   dp[2] = d[1] + dp[1]
                   dp[1] = 1

                   3
        '''
        dp = [n] * (n+1)

        dp[0] = 0

        for i in range(1, n + 1):
            for j in range(1, i+1):
                square = j ** 2

                if i - square  < 0:
                    break
                dp[i] = min(dp[i], dp[i - square] + 1)
        
        return dp[n]

                

        

        
        
        