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
        i = 0
        while i <= len(intervals)-2:
            # check is overlapped ?
            if intervals[i][1] > intervals[i+1][0]:
               count += 1
               intervals[i+1][1] = min(intervals[i][1], intervals[i+1][1])
            i += 1
        
        return count

        