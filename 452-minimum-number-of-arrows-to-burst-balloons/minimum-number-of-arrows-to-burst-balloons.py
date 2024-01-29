class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        '''

                           ------------------
          -------------
        -----------
                    -------------

        1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16

        [1, 6] [2, 8] [7, 12] [10, 16]


        I should shot as many ballon as possible with smallest arrows.

        [1, 2] [3, 4] [5, 6] [7, 8]
        '''

        points.sort()

        prev_end = points[0][1]

        arrow_count = 1
        for start, end in points[1:]:
            # doensn't overlap
            if start > prev_end:
                arrow_count += 1
                prev_end = end
            else: # overlap
                prev_end = min(prev_end, end)
        return arrow_count

