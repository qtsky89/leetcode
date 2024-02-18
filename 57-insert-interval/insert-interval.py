class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # just add
        intervals.append(newInterval)
        
        # sort by start
        intervals.sort(key= lambda x:x[0])

        ret = [intervals[0]]
        # merge
        for i in range(1, len(intervals)):
            # is overlaped? then merge
            if intervals[i][0] <= ret[-1][1]:
                ret[-1][1] = max(intervals[i][1], ret[-1][1])
            else:
                ret.append(intervals[i])
        return ret
        

        
        