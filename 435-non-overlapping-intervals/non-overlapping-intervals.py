class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        1. sort by start time
        2. if there is overlap then, increase count += 1, keep min endtime
           else 
        '''

        # 1. sort by start time
        intervals.sort(key=lambda x:x[0])

        last_end_time = intervals[0][1]
        count = 0
        for i in range(1, len(intervals)):
            # previous interval endtime >= current interval start time
            # there is overlap
            if last_end_time > intervals[i][0]:
                count += 1
                last_end_time = min(last_end_time, intervals[i][1])
            else:
                last_end_time = intervals[i][1]
        return count

