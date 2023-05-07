class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        '''
        len(nums) = 5
        k = 3

        [1  2  3] 4  5
         1 [2  3  4] 5
         1  2 [3  4  5]
        '''
        max_sum = -float('inf')
        tmp_sum = sum(nums[:k])
        for i in range(len(nums)-k+1):
            # TODO. every time calculate the sum, we could imporve it.
            if i != 0:
                tmp_sum = tmp_sum + nums[i+k-1] - nums[i-1]
            max_sum = max(max_sum, tmp_sum)
        
        return max_sum/k
            
