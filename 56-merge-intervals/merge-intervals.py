class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        intervals = [start, end]
        '''
        intervals.sort()

        ret = []
        for i in range(len(intervals)):
            if not ret:
                ret.append(intervals[i])
                continue

            start, end = intervals[i]
            # collapse
            if start <= ret[-1][1]:
                ret[-1][1] = max(ret[-1][1], end)
            else:
                ret.append(intervals[i])
        return ret
