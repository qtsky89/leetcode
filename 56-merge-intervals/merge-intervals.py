class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        example1.
        
                                          --------
                      -----
          --------
        ----
        1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18

        [1, 6] [8, 10] [15, 18]


        intervals = [[1,3],[2,6],[8,10],[15,18]]
                       ^           

        step1. sort by start value
        step2. in for loop, if there is interval then merge, use outside list ret
        step3. return ret
        '''

        intervals.sort()

        ret = []

        last_end_value = -float('inf')
        for i in range(len(intervals)):
            if last_end_value < intervals[i][0]:
                ret.append(intervals[i])
                last_end_value = intervals[i][1]
            # there is overlap
            else:
                ret[-1][1] = max(ret[-1][1], intervals[i][1])
                last_end_value = ret[-1][1]
        return ret

        



