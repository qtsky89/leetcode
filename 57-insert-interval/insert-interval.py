class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        [[1,2],[3,5],[6,7],[8,10],[12,16]]   [4, 8]
          l                         r

        '''

        l, r = 0, len(intervals)-1

        while l<=r:
            m = l + (r-l) // 2

            if intervals[m][0] == newInterval[0]:
                r = m - 1
            elif intervals[m][0] > newInterval[0]:
                r = m - 1
            else:
                l = m + 1
        
        # l is the inserting point

        intervals.insert(l, newInterval)

        ret = []

        for start, end in intervals:
            # it need to be merged
            if ret and ret[-1][1] >= start:
                ret[-1][0] = min(ret[-1][0], start)
                ret[-1][1] = max(ret[-1][1], end)
            else:
                ret.append([start, end])
        
        return ret

        
        