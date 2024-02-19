class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        '''
        [1, 12, -5, -6, 50, 3] k = 4
         p1          p2
            p1          p2
                 p1         p2

        [1, 13, 8, 2, 52, 55]
         ^             ^ => 51 /4


        12, -5, -6, 50

        1. make the accumulate sum array
        2. find the sum in that window
        3. divide by k
        4. return maximum result
        '''
        # 1. make the accumulate sum array
        # [1, 13, 8, 2, 52, 55]
        accumulate_sum = [0] * len(nums)

        accumulate_sum[0] = nums[0]
        for i in range(1, len(accumulate_sum)):
            accumulate_sum[i] = accumulate_sum[i-1] + nums[i]
        
        # 2. find the sum in that window
        p1, p2 = -1, k-1

        ret = -float('inf')
        while p2 <= len(nums)-1:
            if p1 == -1:
                ret = max(ret, accumulate_sum[p2] /k)
            else:
                ret = max(ret, (accumulate_sum[p2] - accumulate_sum[p1]) / k)

            p1, p2 = p1+1, p2+1

        return ret

        

        


