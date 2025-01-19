from collections import deque

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        '''
        a = 1, b = 1, c = 7

        (-1, c)


        c c a c c b c c
        

        '''
        
        # heap = [(-7, c) (-1, a) (-1, b)]
        heap = []
        if a != 0:
            heap.append((-a, 'a'))
        if b != 0:
            heap.append((-b, 'b'))
        if c != 0:
            heap.append((-c, 'c'))
        heapq.heapify(heap)

        cooldown_q = deque()
        
        ret = []
        time = 0 
        # process heap
        while heap or cooldown_q:
            time += 1

            # TODO. pop cooldown_q, push to heap
            if cooldown_q and cooldown_q[0][0] <= time:
                _, data = cooldown_q.popleft()
                heapq.heappush(heap, data)

            if not heap:
                return ''.join(ret)
            
            count, char = heapq.heappop(heap)
            count += 1
            if count < 0:
                if (ret and ret[-1] == char):
                    cooldown_q.append((time+2, (count, char)))
                else:
                    heapq.heappush(heap, (count, char))

            ret.append(char)
                
        return ''.join(ret)