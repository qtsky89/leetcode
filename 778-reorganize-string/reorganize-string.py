from collections import deque

class Solution:
    def reorganizeString(self, s: str) -> str:
        '''
        s = a a a a b b b c c d
               ^
        c = {
            a : 4
            b : 3
            c : 2
            d : 1
        }

        heap = (-4, a), (-3, b) (-2, c) (-1, d)
                  ^
        q = 

        a b a c a b d a b c
        '''

        '''
        c = {
            a : 4
            b : 3
            c : 2
            d : 1
        }
        '''
        c = Counter(s)
        
        '''
        heap = (-4, a), (-3, b) (-2, c) (-1, d)
        '''

        heap = []
        for key, value in c.items():
            heapq.heappush(heap, (-value, key))
        
        cooldown_q = deque()
        ret = []

        time = 0
        # processing the heap
        while heap or cooldown_q:
            time += 1

            # pop item from cooldown_q and push the heap
            if cooldown_q and cooldown_q[0][0] <= time:
                _, (tmp_counter, tmp_char) = cooldown_q.popleft()

                heapq.heappush(heap, (tmp_counter, tmp_char))
            
            if not heap:
                return ""
            
            # -4, a
            count, char = heapq.heappop(heap)
            ret.append(char)

            count += 1

            # push to the cooldown_q
            if count != 0:
                cooldown_q.append((time+2, (count, char)))
            

        return ''.join(ret) if len(ret) == len(s) else ""

            
        
        