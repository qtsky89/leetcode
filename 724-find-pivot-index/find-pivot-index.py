class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        '''
        nums = 1 7 3 6 5 6 
                              left: 0, right: 28
               ^              left: 0, right: 27
                 ^            left: 1, right: 20
                   ^          left: 8, right: 17
                     ^        left: 11, right: 11,  return 3
        '''

        left_sum = 0
        right_sum = sum(nums)

        for i in range(len(nums)):
            left_sum += nums[i-1] if i-1 >=0 else 0
            right_sum -= nums[i]

            if left_sum == right_sum:
                return i
        return -1