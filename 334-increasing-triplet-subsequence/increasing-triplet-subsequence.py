class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        '''
        i < j < k , nums_i < nums_j < nums_k

        nums = [2, 1, 5, 0, 4, 6]
                ^                 nums_i = 2
                   ^              nums_i = 1
                      ^           nums_i = 1 nums_j=5
                         ^        nums_i = 0 nums_j=5
                            ^     nums_i = 0 nums_j=4
                               ^  nums_i = 0 nums_j=4 nums_k=6

        '''

        nums_i, nums_j = float('inf'), float('inf')
        for n in nums:
            if n <= nums_i:
                nums_i = n
            elif n <= nums_j:
                nums_j = n
            else:
                return True
        
        return False



