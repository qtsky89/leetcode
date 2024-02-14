class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        '''
        example1.
            intervals = [[0,30],[5,10],[15,20]]
        '''

        # intervals = [[0,30],[5,10],[15,20]]
        intervals.sort()

        # heap can have end values only
        heap = []
        max_heap_count = 0
        for interval in intervals:
            # there is ended meeting room
            if heap and heap[0] <= interval[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, interval[1])
            
            max_heap_count = max(max_heap_count, len(heap))
        
        return max_heap_count
            

        