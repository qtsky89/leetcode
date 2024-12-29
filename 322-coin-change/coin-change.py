class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        count_map = {
            5 : 1
            2 : 1
            1 : 1
        }

        '''

        coins.sort(reverse=True)

        count_map = {}

        def dfs(current_sum: int, coin_count: int) -> None:
            if current_sum > amount:
                return

            if current_sum in count_map and count_map[current_sum] <= coin_count:
                return
            
            count_map[current_sum] = coin_count
                
            for coin in coins:
                dfs(current_sum+coin, coin_count+1)

        dfs(0, 0)

        return count_map[amount] if amount in count_map else -1
        