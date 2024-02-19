class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        '''
        pivot index
        nums =      [ 1, 7, 3, 6, 5, 6  ]
        left_sum =  [ 0  1  8  11 17 22 ]                  
     right_sum =    [ 27 20 17 11 6  0 ]
                 ^                 0, 27
                    ^              1, 20
                       ^           8, 17
                          ^        11  11 => return 3
                                   17  6
                                   22  0
        '''

        left_sum = [0] * len(nums)
        right_sum = [0] * len(nums)

        left_sum[0] = nums[0]
        for i in range(1, len(nums)):
            left_sum[i] = left_sum[i-1] + nums[i]
        
        left_sum.insert(0, 0)
        left_sum.pop()
        
        right_sum[-1] = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            right_sum[i] = right_sum[i+1] + nums[i]
        
        right_sum.pop(0)
        right_sum.append(0)

        for i in range(len(nums)):
            if left_sum[i] == right_sum[i]:
                return i
        return -1
        