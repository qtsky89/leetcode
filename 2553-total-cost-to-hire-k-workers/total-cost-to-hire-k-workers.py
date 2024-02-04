class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        '''
        example.
        costs = [17, 12, 10, 2, 7, 2, 11 ,20, 8]
                               stack1 = [7, 2, 11, 20, 8] reverse
                               stack2 = [17, 12, 10, 2, 7]

        1. first session: 2
            heap = [17, 12, 10 ] +  [2, 11, 20, 8] => 2
        2. second session: 2
            heap = [17, 12, 10, 7] [2, 11, 20, 8] => 2
        3. third session: 7

        k = 3 <- worker
        candidates = 4       


        0 1 2 3 4 5
            ^
            6 - 1 - 5 => 
                
        '''
        # step1. make heap1, heap2, stack1, stack2
        heap1 = costs[:candidates]
        heapq.heapify(heap1)
        p1 = candidates-1

        heap2 = costs[max(len(costs)-candidates, p1+1):]
        heapq.heapify(heap2)
        p2 = len(costs) - candidates
        
        total_costs = 0
        while k > 0:
            first_tmp = heap1[0] if heap1 else float('inf')
            second_tmp = heap2[0] if heap2 else float('inf')

            if first_tmp <= second_tmp:
                total_costs += heapq.heappop(heap1)
                
                if p1+1 < p2:
                    p1 += 1
                    heapq.heappush(heap1, costs[p1])
                    
            else:
                total_costs += heapq.heappop(heap2)
                
                if p2-1 > p1:
                    p2 -= 1
                    heapq.heappush(heap2, costs[p2])
            k-=1
        return total_costs