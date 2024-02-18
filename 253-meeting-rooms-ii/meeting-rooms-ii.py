class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        '''
        min_end_heap = []


        1. sort by start time
        2. keep min_end_heap
        3. whenever new interval comes in, check with min end value
            if min_end_value <= new_interval_start:
               i don't need meeting room
            else
               i need new meeting room.
            update min_end_value
        '''    

        # 1. sort by start time
        intervals.sort(key=lambda x:x[0])

        # 2. keep min_end_heap
        heap = [intervals[0][1]]

        # 3. whenever new interval comes in, check with min end value
        count = 1
        for i in range(1, len(intervals)):
            min_end_time = heap[0]
            # i don't need meeting room
            if min_end_time <= intervals[i][0]:
                heapq.heappop(heap)
            else: # i need new meeting room
                count += 1
            heapq.heappush(heap, intervals[i][1])
        return count

                