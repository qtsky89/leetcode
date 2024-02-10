class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
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
        '''

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