class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        11. Container with most water

        1. formuala to water amount = > min(height[i], height[j]) * (j-i)
        
        2. if height[i] < height[j]: i+=1
            else:
                j-=1 until i < j
        '''

        i, j = 0, len(height)-1

        max_value = 0
        while i < j:
            max_value = max(max_value, min(height[i], height[j]) * (j-i))

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_value


        