class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        nums = 2 3 -2   4  5  0  -1  -2  4
         1     2      
         1     1 

        '''
        ret = max(nums)

        max_so_far = 1
        min_so_far = 1

        for n in nums:
            max_so_far, min_so_far = max(n, max_so_far * n, min_so_far * n), min(n, max_so_far * n, min_so_far * n)

            ret = max(ret, max_so_far)

        return ret