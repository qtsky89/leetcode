class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        '''

        ret: list[list] = []

        for, while loop intervals

            if interval[0] < newInterval:
                push to ret
            else:
                merge or just push
        
        return ret
        '''

        intervals.append(newInterval)
        intervals.sort()

        ret: list[list[int]] = []

        for interval in intervals:
            # no overlap
            if not ret or ret[-1][1] < interval[0]:
                ret.append(interval)
            else: #overlap
                ret[-1][1] = max(ret[-1][1], interval[1])
        
        return ret



