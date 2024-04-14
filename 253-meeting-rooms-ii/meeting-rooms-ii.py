class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        '''
        step1. sort by start time, end time
        step2. min heap <= endtime

            if min_endtime <  start time => I can reuse the meeting
            else:
                increase the meeting room count
                I put end time to the heap
        '''

        # step1. sort by start time, end time
        intervals.sort()

        # step2. min heap <= start_time
        heap = []

        meeting_room_count = 0
        for start, end in intervals:
            # I don't need new meeting
            if heap and heap[0] <= start:
                heapq.heappop(heap)
                heapq.heappush(heap, end)
            else:
                meeting_room_count += 1
                heapq.heappush(heap, end)
        return meeting_room_count