class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        c = {
            A : 3
            B : 3
        }

        heap = [(-3, A), (-3, B)]

        A B idle A B idle A B

        
        '''

        c = Counter(tasks)
        
        heap = []

        for key, value in c.items():
            heapq.heappush(heap, (-value, key))
        
        cooldown_q = deque()
        # [time, item]

        time = 0
        while heap or cooldown_q:
            time += 1

            if cooldown_q and cooldown_q[0][0] <= time:
                _, item = cooldown_q.popleft()
                heapq.heappush(heap, item)
            
            if not heap:
                continue

            count, char = heapq.heappop(heap)
            count += 1

            if count == 0:
                continue
            else:
                cooldown_q.append([time+n+1, (count, char)])
            
        return time

