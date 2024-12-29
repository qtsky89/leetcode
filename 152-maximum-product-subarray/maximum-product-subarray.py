class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        '''

        -4, -12, 24

        nums =   -2   3   -4
        c_max 1  -2   3    24
        c_min 1  -2   -6   -12

        c_max = max(nums[i], c_max * nums[i], c_min * nums[i])
        c_min = min(nums[i], c_max * nums[i], c_min * nums[i])
        '''

        c_max, c_min = 1, 1

        ret = max(nums)
        for n in nums:
            c_max, c_min = max(n, c_max * n, c_min * n), min(n, c_max * n, c_min * n)

            ret = max(ret, c_max)
        
        return ret
            



        