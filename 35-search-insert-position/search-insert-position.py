class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        '''
        nums = 1, 3, 5, 6     target=5
                     ^        ret = 2
        
        nums = 1, 3, 5, 6      target = 2
                  ^            ret = 1
        
        nums = 1, 3, 5, 6      target = 7
                          ^    ret = 4
        '''

        l, r = 0, len(nums)-1

        while l <= r:
            m = l + (r-l) // 2

            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        
        return l