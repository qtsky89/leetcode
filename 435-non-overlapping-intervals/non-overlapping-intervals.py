class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        intervals
    
        intervals[i] = 

        

        exmaple1.

            
                        <          >
                    <                   >
                <      >
            <               >      
        0   1   2   3   4   5   6   7   8   9  10

        count += 1

        [1, 5] [2, 4] [3, 8] [3, 10] [4, 7]   count = 1

        step1. sort
        step2. using for loop, if overlapped, remove the end is bigger one
        '''

        if len(intervals) == 1:
            return 0

        intervals.sort()
        
        count = 0
        i = 1

        last_end = intervals[0][1]
        while i <= len(intervals)-1:
            # check is overlapped ?
            if last_end > intervals[i][0]:
                count += 1
                last_end = min(last_end, intervals[i][1])
            else:
                last_end = intervals[i][1]
            i += 1
        
        return count

        