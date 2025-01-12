class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        '''
        tasks => [1, 2, 0] [2, 4, 1] [3, 2, 2] [4, 1, 3]

        tasks.sort() => [1, 2, 0] [2, 4, 1] [3, 2, 2] [4, 1, 3]
        
        time = 1

        heap = [(2, 0),]
                  ^
        process_time, index = heappop(heap)

        ret.append(index)

        '''

        # push original index
        for index, t in enumerate(tasks):
            t.append(index)
        
        # sort by enqueue time
        tasks.sort(key=lambda x:x[0])

        # (process_time, index)
        heap: list[tuple[int, int]] = []

        i = 0
        ret = []
        time = 0

        while len(ret) < len(tasks):
            while i <= len(tasks)-1:
                if tasks[i][0] <= time:
                    heapq.heappush(heap, (tasks[i][1], tasks[i][2]))
                    i += 1
                else:
                    break
            
            if not heap:
                time = tasks[i][0]
                continue

            process_time, org_index = heapq.heappop(heap)
            ret.append(org_index)

            time += process_time
            
        return ret
        