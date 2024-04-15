class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        ret = []
        for i in range(len(intervals)):
            # overlapping
            if ret and ret[-1][1] >= intervals[i][0]:
                ret[-1][1] = max(ret[-1][1], intervals[i][1])
            else:
                ret.append(intervals[i])
        return ret
                