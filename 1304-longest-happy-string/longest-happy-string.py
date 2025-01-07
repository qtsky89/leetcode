class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        '''
        example1.
            a => 1
            b => 1
            c => 7

            ''
            'a'
            'b'
            'c'

            'ab'
            'bc'
            'ab'

            'abc'
            'abcc'
            'abccc' => X
                 ^
            'ccaccbcc' => O

            heap = (-7, 'c'), (-1, 'a'), (-1, 'c')
            
            => cccccccba
        '''
        heap = []

        if a != 0:
            heap.append((-a, 'a'))
        if b != 0:
            heap.append((-b, 'b'))
        if c != 0:
            heap.append((-c, 'c'))
        
        # heap = (-7, 'c'), (-1, 'a'), (-1, 'c')
        '''
            ret = c c 
                    ^
            q = (count, c)
        '''
        heapq.heapify(heap)

        # cool down queue (after 2times, it will cooldown in here for one iteration)
        q = deque()

        time = 0
        ret = []
        while heap or q:
            time += 1

            while q and q[0][2] <= time:
                count, char, _ = q.popleft()
                heapq.heappush(heap, (count, char))
            
            if not heap:
                return ''.join(ret)

            count, char = heappop(heap)
            count += 1

            # need to cool down
            if count != 0:
                if ret and ret[-1] == char:
                    q.append((count, char, time+2))
                else:
                    heappush(heap, (count, char))
        
            ret.append(char)

        return ''.join(ret)

