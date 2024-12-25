from collections import defaultdict, deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        '''
        adjacent_map = {
            0 : [(1, 100)]
            1 : [(2, 100), (3, 600)]
            2 : [(0, 100), (3, 100)]
            3 : [()]
        }

        min_prices = {
            0 : inf
            1 : inf
            2 : inf
            3 : inf
        }

        0 -> 3
        '''

        adjacent_map: defaultdict[int, list[tuple[int, int]]] = defaultdict(list)

        for start, end, cost in flights:
            adjacent_map[start].append((end, cost))
        
        min_prices = {i: float('inf') for i in range(n)}
        
        q = deque([(src, 0, 0)])
        while q:
            # current_city = 0, current_cost = 0, current_stop_count = 0
            current_city, current_cost, current_stop_count = q.popleft()

            if current_stop_count > k+1:
                continue
            
            min_prices[current_city] = min(min_prices[current_city], current_cost)
            if current_city == dst:
                continue

            for next_city, cost in adjacent_map[current_city]:
                if current_cost+cost < min_prices[next_city]:
                    q.append((next_city, current_cost+cost, current_stop_count+1))

        return min_prices[dst] if min_prices[dst] != float('inf') else -1
        
        
        