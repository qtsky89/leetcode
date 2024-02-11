class Solution:
    # nlogn solution
    '''
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        

        ret: list[list] = []

        for, while loop intervals

            if interval[0] < newInterval:
                push to ret
            else:
                merge or just push
        
        return ret

        n log n solution
        

        intervals.append(newInterval)
        intervals.sort()

        ret: list[list[int]] = []

        for interval in intervals:
            # no overlap
            if not ret or ret[-1][1] < interval[0]:
                ret.append(interval)
            else: #overlap
                ret[-1][1] = max(ret[-1][1], interval[1])
        
        return ret'''

    # O(n) solution https://youtu.be/A8NUOmlwOlM
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        

        ret = []

        for i in range(len(intervals)):
            # there is no overlap
            if newInterval[1] < intervals[i][0]: 
                ret.append(newInterval)
                return ret + intervals[i:]
            
            if newInterval[0] > intervals[i][1]:
                ret.append(intervals[i])
            else:
                newInterval = ([min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])])
        
        ret.append(newInterval)

        return ret
