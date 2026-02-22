from heapq import heappush, heappop, heapify

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        count = [0] * n
        
        idle_meeting_room = [i for i in range(n)] # elements are meeting room numbers
        heapify(idle_meeting_room)
        busy_meeting_room = []       

        meetings.sort()

        '''
        meetings = [[0,10],[1,5],[2,7],[3,4]]
                     ^
        count =  [0, 0]

        idle_meeting_room = [0, 1]
        busy_meeting_room = [[0, 0], [0, 1]] first one end time, second one meeting room number

        '''

        for start, end in meetings:
            # release busy first and push to idle room
            while busy_meeting_room and busy_meeting_room[0][0] <= start:
                _, meeting_room_num = heappop(busy_meeting_room)
                heappush(idle_meeting_room, meeting_room_num)

            # use idle meeting first
            if idle_meeting_room:
                meeting_room_num = heappop(idle_meeting_room)
                
                # update count array
                count[meeting_room_num] += 1

                heappush(busy_meeting_room, [end, meeting_room_num])
            else:
                # use meeting room
                end_time, meeting_room_num = heappop(busy_meeting_room)
                
                # update count array
                count[meeting_room_num] += 1

                # can use it right away
                # end_time = 5, start = 2
                heappush(busy_meeting_room, [end + (end_time - start), meeting_room_num])

        max_count = max(count)

        for i in range(len(count)):
            if count[i] == max_count:
                return i
                
        