class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        '''
        tasks = [[1,2],[2,4],[3,2],[4,1]]
                   ^
        q = [[1,2],[2,4],[3,2],[4,1]]
               ^
        heap = [(2, 1, 1), ]


        tasks = [enqueue_time, process_time, index]
        heapValue = [process_time, index, enqueue_time]
        '''

        for index, task in enumerate(tasks):
            task.append(index)
        
        # sort by enqueue time
        tasks.sort(key=lambda x:x[0])

        heap = []
        time = tasks[0][0]
        ret = []

        i = 0
        while i <= len(tasks)-1 or heap:
            while i <= len(tasks)-1 and tasks[i][0] <= time:
                enqueue_time, process_time, index = tasks[i]
                heapq.heappush(heap, (process_time, index))
                i+=1
            
            if heap:
                process_time, index = heapq.heappop(heap)
                time += process_time
                ret.append(index)
            else:
                time = tasks[i][0]

        return ret
            
            

        
