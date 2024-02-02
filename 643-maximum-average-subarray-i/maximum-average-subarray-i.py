class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        p = 0
        '''
        k = 4

        sum[i:i+k] = accumuate_sum[0+k-1] - accumulate_sum[i-1]

        [1, 12, -5, -6, 50, 3]
         1  13  8   2   52  53

         0  1   2   3   4   5


        [            ]
            [            ]
               [            ]   2+4 
        '''

        accumulate_sum = [0] * len(nums)
        accumulate_sum[0] = nums[0]
        for i in range(1, len(nums)):
            accumulate_sum[i] = accumulate_sum[i-1] + nums[i]

        max_val = -float('inf')
        while p + k <= len(nums):
            sum_data = accumulate_sum[p+k-1] - (accumulate_sum[p-1] if p-1 >= 0 else 0)
            max_val = max(max_val, sum_data / k)
            p += 1
        return max_val
