from heapq import heappush

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        tasks = A A A B B B n = 2

        efficient way to choose is select high frequency label

        A -> B -> idle -> A -> B -> idle -> A -> B


        counter = {
            A : 3
            B : 3
        }

        heap = (-3, A) (-3, B)

                

        q = deque( [(-2, A), 2] )
        

        time: O(N), space: O(N)
        '''

        counter = Counter(tasks)
        heap = []
        for key, value in counter.items():
            heappush(heap, (-value, key))
        
        # whenever spcific CPU is used, it cool down in this q
        q = deque()

        time = 0
        while heap or q:
            time += 1
            # put heap when the cool down q meet time
            if q and q[0][1] <= time:
                item = q.popleft()
                heappush(heap, item[0])
                       
            if heap:
                (count, label) = heappop(heap)
                if count + 1 != 0:
                    q.append([(count+1, label), time+n+1])
        return time
            

        
        