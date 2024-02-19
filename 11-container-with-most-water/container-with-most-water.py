class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        (p2 - p1) * min(height[p1], height[p2])

        height = [ 1, 8, 6, 2, 5, 4, 8, 3, 7 ]
                   p1                      p2
                      p1                   p2

                      if height[p1] < height[p2] p1 += 1
                      else p2 -=1
        '''

        p1, p2 = 0, len(height)-1

        ret = 0
        while p1 < p2:
            ret = max(ret, (p2 - p1) * min(height[p1], height[p2]))

            if height[p1] < height[p2]:
                p1 += 1
            else:
                p2 -= 1
        return ret
