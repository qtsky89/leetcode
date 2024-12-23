class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        '''
        there are n cities

        example1.
        n=4 0, 1, 2, 3

        src = 0, dist = 3 k=1

        # step1. let make this hash_map
        {
            2 : [ [0, 100], [3, 200]  ]
        }
        '''
        # step1. let make this hash_map
        hash_map = {}
        for i in range(len(flights)):
            from_i, to_i, price_i = flights[i]

            if from_i in hash_map:
                hash_map[from_i].append([to_i, price_i])
            else:
                hash_map[from_i] = [[to_i, price_i]]
            

        prices = [float('inf')] * n
        q = deque([[src, 0, 0]])

        while q:
            current_city, current_cost, current_stop = q.popleft()

            prices[current_city] = min(prices[current_city], current_cost)

            if current_city == dst:
                continue

            if current_stop > k:
                continue
            
            if current_city in hash_map:
                for next_city, cost in hash_map[current_city]:
                    if current_cost + cost < prices[next_city]:
                        q.append([next_city, current_cost + cost, current_stop+1])
        return prices[dst] if prices[dst] != float('inf') else -1
            