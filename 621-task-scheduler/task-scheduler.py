class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        c = {
            A : 3
            B : 3
            C : 2
            D : 1
        }
        [[-3, A], [-3, B] ...]

        n = 3
        '''

        heap = []
        c = Counter(tasks)
        for key in c:
            heapq.heappush(heap, [-c[key], key])
        
        q = deque()
        time = 0
        while heap or q:
            time += 1

            if q and q[0][0] <= time:
                heapq.heappush(heap, q.popleft()[1])
            
            if not heap:
                continue

            val, key = heapq.heappop(heap)

            if val+1 < 0:
                q.append([time+n+1 ,[val+1, key]])
            
        return time
            
