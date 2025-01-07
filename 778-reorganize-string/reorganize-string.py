class Solution:
    def reorganizeString(self, s: str) -> str:
        '''
        s = aaaabbbccd

        c = {
            a : 4
            b : 3
            c : 2
            d : 1
        }

        time = 0
        heap = (-4, a), (-3, b) (-2, c) (-1, d)

        q = deque()

        => a b a b a c a b c d
        '''

        c = Counter(s)
        
        heap = []
        for key in c:
            heap.append((-c[key], key))
        
        heapq.heapify(heap)
        
        q = deque()
        time = 0

        ret = ""
        while heap or q:
            time += 1
            while q and q[0][0] <= time:
                time, count, key = q.popleft()

                heapq.heappush(heap, (count, key))
            
            if heap:
                count, key = heapq.heappop(heap)
                ret += key
                count += 1

                if count < 0:
                    q.append((time+2, count, key))
            else:
                return ""
        return ret
        

        


            

        
        