def key_function(x: list[int]):
    return x[0]


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        intervals[i] = [start, end]

        1 -> 2 -> 3 -> 4 

        '''

        intervals.sort(key=key_function)
        
        removal_count = 0
        i = 1

        end_value = intervals[0][1]

        while i <= len(intervals)-1:
            # overlapped with next interval
            if end_value > intervals[i][0]:
                end_value = min(end_value, intervals[i][1])
                removal_count += 1
            else:
                end_value = intervals[i][1]
            i += 1
        return removal_count
                