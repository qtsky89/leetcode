class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        coins = 1, 2, 5 amount = 13
                5 + 5 + 2 + 1
    
        dp[13] => dp[8] + 1
               => dp[11] + 1
               => dp[12] + 1
        

        1 2 3 4 5 6 7 8 9 10 11 12 13
                                    ^
                      ^
            ^
        ^
        '''

        '''
        {
            1 : 1
            2 : 1
            5 : 1
        }
        '''

        if amount == 0:
            return 0

        dp = {coin: 1 for coin in coins}

        def dfs(n: int) -> int:
            if n in dp:
                return dp[n]
            
            candidates = []
            for coin in coins:
                if n - coin >= 0:
                    tmp = dfs(n - coin)
                    if tmp >= 0:
                        candidates.append(tmp + 1)
            
            if candidates:
                dp[n] = min(candidates)
            else:
                dp[n] = -1

            return dp[n]
        
        return dfs(amount)
