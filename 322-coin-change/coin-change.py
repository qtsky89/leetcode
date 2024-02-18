class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        q = deque()

        for coin in coins:
            q.append([1, coin])
        
        visited = set()
        while q:
            current_count, current_amount = q.popleft()
            visited.add(current_amount)
            if current_amount == amount:
                return current_count
            elif current_amount > amount:
                continue
            
            for coin in coins:
                if current_amount + coin not in visited:
                    visited.add(current_amount + coin)
                    q.append([current_count+1, current_amount + coin])
        
        return -1
        

        