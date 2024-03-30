class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        '''
        [0, 30]
        [5, 10]
        [15, 20]
        '''

        intervals.sort()

        end_time_heap = []
        count = 0

        for start, end in intervals:
            # check I can reuse meeting room
            if end_time_heap and end_time_heap[0] <= start:
                heapq.heappop(end_time_heap)
                heapq.heappush(end_time_heap, end)
            else:
                count += 1
                heapq.heappush(end_time_heap, end)
        return count
        