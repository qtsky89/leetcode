class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        height = 1 8 6 2 5 4 8 3 7
                 ^               ^
                 l               r
                 0               8
                 min(hieght[l], height[r]) * (r-l) => 9

        '''

        l, r = 0, len(height)-1

        max_area = 0
        while l < r:
            current_area = min(height[l], height[r]) * (r-l)
            max_area = max(max_area, current_area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area

            