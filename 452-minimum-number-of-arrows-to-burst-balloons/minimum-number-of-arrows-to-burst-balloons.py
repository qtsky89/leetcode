class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        '''
        there are some spherical ballon 

        
        

        example.1
                             ------------------
            ------------
          -----------
                      -------------                 
        0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 

        let's try start

        [1, 6] [2, 8] [7, 12] [10, 16]

        I need to do min shot, 
        


        example2.
        [1, 2] [3, 4] [5, 6] [7, 8]

        example3.
        [1, 2] [2, 3] [3, 4] [4, 5]

        
        step1. first sort by first and second element
        step2. if there is interval between, two ballon, add count then keep the min
        step3. just go thorugh if that min is interval, then keep add count
        '''

        points.sort()
        
        prev_end = points[0][1]

        count = 1
        # prev_end = 6
        # [2, 8]
        for i in range(1, len(points)):
            # if interval
            if prev_end >= points[i][0]:
                prev_end = min(prev_end, points[i][1])
            else:
                prev_end = points[i][1]
                count += 1
        return count