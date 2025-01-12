class Solution:
    def reorganizeString(self, s: str) -> str:
        '''
        s =  a a a a b b b c c d

             a b a b a c a b c d
        
        count_map = {
            a: 4
            b: 3
            c: 2
            d: 1  
        }

        heap = [(-4, a), (-3, b), (-2, c), (-1, d)]

        1. use highest count as possible
        2. don't use same character again
        '''

        '''
        count_map = {
            a: 4
            b: 3
            c: 2
            d: 1  
        }
        '''
        count_map = Counter(s)

        # heap = [(-4, a), (-3, b), (-2, c), (-1, d)]
        heap = []
        for key, value in count_map.items():
            heap.append((-value, key))
        heapq.heapify(heap)
        
        # to cooldown previous used character
        # cooldown_q = [(time, (-4, a)), ...]
        cooldown_q = deque()
        ret = []

        time = 0

        while heap or cooldown_q:
            time += 1
            if cooldown_q and cooldown_q[0][0] <= time:
                _, data = cooldown_q.popleft()
                
                heapq.heappush(heap, data)
            
            if not heap:
                return ""
            
            count, char = heapq.heappop(heap)
            ret.append(char)
            count += 1

            if count < 0:
                cooldown_q.append((time+2, (count, char)))
            
        return ''.join(ret)
            
            



                
        
