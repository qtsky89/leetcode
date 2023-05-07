class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        1  8  6  2  5  4  8  3  7
        ^p1                     ^p2
        '''

        p1, p2 = 0, len(height)-1

        ret = 0
        while p1 < p2:
            if height[p1] < height[p2]:
                area = (p2 - p1) * height[p1]
                ret = max(ret, area)
                p1 += 1
            else:
                area = (p2 - p1) * height[p2]
                ret = max(ret, area)
                p2 -= 1
        return ret


            
        