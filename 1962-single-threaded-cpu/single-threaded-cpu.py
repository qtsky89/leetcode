class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        '''
        [1, 2]
        [2, 4]
        [3, 2]
        [4, 1]


        time = 1
            [1, 2]
        
        time = 3
            [2, 4] [3, 2]
                       ^
        time = 5
            [2, 4] [4, 1]
                      ^
        time = 9
            [2, 4]
              ^
        time = 11
            no job left

        => [0, 2, 3, 1]

        tasks = [[1, 2, 0], [2, 4, 1], [3, 2, 2], [4, 1, 3]]

        make a heap = [(2, 0) ]
                         ^
        '''

        # tasks = [[1, 2, 0], [2, 4, 1], [3, 2, 2], [4, 1, 3]]
        for i, t in enumerate(tasks):
            t.append(i)
        
        # sort by enqueue time
        tasks.sort(key=lambda x:x[0])
        
        # make a heap = [(2, 0) ]
        #                  ^
        i = 0
        heap = []
        ret = []
        time = tasks[0][0]

        while len(ret) < len(tasks):
            # pop from tasks, push to the heap
            while i <= len(tasks)-1 and tasks[i][0] <= time:
                # push (process_time, index)
                heapq.heappush(heap, (tasks[i][1], tasks[i][2]))
                i += 1
            
            if not heap:
                time = tasks[i][0]
            else:
                process_time, index = heapq.heappop(heap)

                ret.append(index)

                time += process_time
        

        return ret
        
