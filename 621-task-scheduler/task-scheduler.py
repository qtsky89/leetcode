from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        tasks = A A A B B B , n=2
        
        # step 1 counter (hashmap)
        c = {
            A : 3
            B : 3
        }

        # step 2 min heap
        heap = [(-3, 'A'), (-3, 'B')]


        # step 3, while loop processing heap, cooldown_q
        while 

        cooldown_q = [(n+1 , (-2, A'))]


        '''


        '''
        tasks = A A A B B B , n=2
        
        # step 1 counter (hashmap)
        c = {
            A : 3
            B : 3
        }
        '''
        c = Counter(tasks)

        '''
        # step 2 min heap
        heap = [(-3, 'A'), (-3, 'B')]
        '''
        heap = []

        for key in c:
            heap.append((-c[key], key))
        
        heapq.heapify(heap)

        # step 3, while loop processing heap, cooldown_q

        cooldown_q = deque()
        time = 0
        while heap or cooldown_q:
            time += 1
            # TODO. push back to heap from cooldown_q
            while cooldown_q and cooldown_q[0][0] <= time:
                _, data = cooldown_q.popleft()
                heapq.heappush(heap, data)

            # idle
            if not heap:
                continue
            
            count, char = heapq.heappop(heap)

            count += 1

            if count != 0:
                cooldown_q.append((time+n+1, (count, char)))
        

        return time
                



