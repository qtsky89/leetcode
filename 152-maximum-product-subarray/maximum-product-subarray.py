class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        nums = [2 , 3, -2, 4]    keep the 
       cur_max  2   6
       cur_min  2   
        '''

        res = max(nums)

        cur_min, cur_max = 1, 1

        for n in nums:
            if n == 0:
                cur_min, cur_max = 1, 1
                continue
            
            cur_max, cur_min = max(n * cur_max, n * cur_min, n), min(n * cur_max, n * cur_min, n)
            res = max(res, cur_max)
        
        return res
        
