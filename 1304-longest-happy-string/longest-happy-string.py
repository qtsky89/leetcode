from collections import deque

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        '''
        a = 1, b = 1, c = 7

        {
            a : 1
            b : 1
            c : 7
        }

        => [(-7, c) (-1, a) (-1, b)]

        c c a 
        '''

        # make min heap (reversed sign)
        heap = []
        if a != 0:
            heap.append((-a, 'a'))
        if b != 0:
            heap.append((-b, 'b'))
        if c != 0:
            heap.append((-c, 'c'))
        heapq.heapify(heap)

        # make cooldown queue
        # q = [(time, (-7, c)), ...]
        q = deque()

        ret = []
        time = 0
        while heap or q:
            time += 1

            # push back in the heap
            if q and q[0][0] <= time:
                _, data = q.popleft()
                heapq.heappush(heap, data)
            
            # process heap
            # => [(-7, c) (-1, a) (-1, b)]
            if not heap:
                break
            count, char = heapq.heappop(heap)
            
            count += 1
            if count < 0:
                if (ret and ret[-1] == char):
                    q.append((time+2, (count, char)))
                else:
                    heapq.heappush(heap, (count, char))
            ret.append(char)

        return ''.join(ret)
            
            






        

        