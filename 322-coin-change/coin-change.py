class Solution:

    # this is BFS solution
    '''
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        coins = [1, 2, 5] amount = 11

        => [1, 1, 1, 1, ....] => 11
           [1, 2, ....] =>
           [5, 5, 1] => 

        step1. using queue, check every possibility
        [5, 5, 1] [5, 2] [5, 1]
        [2] 
        [1]

        step2. in while loop, don't do when sum of coins is in visited

        step3. return length of current_coin when it reach the amount
        

        if amount == 0:
            return 0

        inputs = []
        for i in range(len(coins)):
            inputs.append([1, coins[i]])

        q = deque(inputs)

        visited = set()

        while q:
            length, total = q.popleft()

            visited.add(total)

            if total == amount:
                return length
            elif total > amount:
                continue
            
            for i in range(len(coins)):
                if total + coins[i] not in visited and total + coins[i] <= amount:
                    visited.add(total + coins[i])
                    q.append([length+1, total + coins[i]])
        
        return -1
        '''

    # https://youtu.be/H9bfqozjoqs?si=LVodgTqFrE5xl4fg dp solution
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        dp[3] = 2
        dp[4] = 2
        dp[5] = 1
        dp[6] = dp[5] + dp[1] ...

        dp[n] = dp[n - coin] + 1
        '''

        dp = [float('inf')] * (amount + 1)
        dp[0] = 0 

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i-coin] +1)
        
        return dp[-1] if dp[-1] != float('inf') else -1








        return -1