class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        '''
                          p1  p2
        costs = [1,2,4,1], k = 3, candidates = 3

        '''

        p1= candidates-1
        p2 = len(costs)-candidates

        first_min_heap = costs[:p1+1]
        last_min_heap = costs[max(len(costs)-candidates, p1+1):]

        heapq.heapify(first_min_heap)
        heapq.heapify(last_min_heap)

        total = 0
        for i in range(k):
            first_tmp = first_min_heap[0] if first_min_heap else float('inf')
            second_tmp = last_min_heap[0] if last_min_heap else float('inf')

            if first_tmp <= second_tmp:
                total += heapq.heappop(first_min_heap)

                if p1+1 < p2:
                    p1 += 1
                    heapq.heappush(first_min_heap, costs[p1])
            else:
                total += heapq.heappop(last_min_heap)
                
                if p2-1 > p1:
                    p2 -= 1
                    heapq.heappush(last_min_heap, costs[p2])
        return total

        
