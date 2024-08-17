class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        height = 1 8 6 2 5 4 8 3 7
        '''

        p1, p2 = 0, len(height)-1

        max_area = 0

        while p1 < p2:
            max_area = max(min(height[p1], height[p2])*(p2-p1), max_area)

            if height[p1] < height[p2]:
                p1 += 1
            else:
                p2 -= 1
        return max_area