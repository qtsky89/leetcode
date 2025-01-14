class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        '''
        nums = 1, 7, 3, 6, 5, 6
                                   left: 0, right: 28
               ^                   left: 0, right: 27
                  ^                left: 1, right: 20
                     ^             left: 8, right: 17
                        ^          left:11, right: 11
        '''

        left, right = 0, sum(nums)

        for i in range(len(nums)):
            right -= nums[i]

            left += (nums[i-1] if i-1 >= 0 else 0)

            if left == right:
                return i
        
        return -1