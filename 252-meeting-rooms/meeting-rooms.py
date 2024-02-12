class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        '''
        if there are no overlapping, return True
        else
            return False

        step1. sort ! by start time
        step2. if previous interval end time > current intervals start time => overlapping
               else we can continue
        '''

        intervals.sort()

        for i in range(1, len(intervals)):
            # if previous interval end time > current intervals start time => overlapping
            # ovelapping
            if intervals[i-1][1] > intervals[i][0]:
                return False
        return True
        