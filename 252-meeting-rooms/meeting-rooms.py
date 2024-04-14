class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        '''
        step1. sort intervals (start_time, end_time)
        step2. if collapse it means last end_time > new start_time return False
               else return True
        '''

        intervals.sort()

        for i in range(1, len(intervals)):
            # collapse
            if intervals[i-1][1] > intervals[i][0]:
                return False
        
        return True
