class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''

        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
                  ^                       ^
        p1 = 0
        p2 = 8

        1.  (p2 - p1) * min(p2, p1)
        '''

        p1, p2= 0, len(height)-1

        max_water_size = 0
        while p1 < p2:
            water_size = (p2-p1) * min(height[p1], height[p2])
            max_water_size = max(max_water_size, water_size)

            if height[p1] < height[p2]:
                p1 += 1
            else:
                p2 -= 1
        return max_water_size