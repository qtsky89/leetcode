class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        '''
        nums = [1, 7, 3, 6, 5, 6]

        l_sum = [1,  8,  11, 17, 22, 28]
        r_sum = [28, 27, 20, 17, 11, 6]

        pivot[0] => left: 0,       right: r_sum[1]
        pivot[1] => left: l_sum[0], right: r_sum[2]
        pivot[2] => left: l_sum[1], right: r_sum[3]
        pivot[3] => left: l_sum[2], right: r_sum[4]
        pivot[4] => left: l_sum[3], right: r_sum[5]
        pivot[5] => left: l_sum[4], right: 0
        '''

        l_sum = [0] * len(nums)
        l_sum[0] = nums[0]

        for i in range(1, len(l_sum)):
            l_sum[i] = l_sum[i-1] + nums[i]

        r_sum = [0] * len(nums)
        r_sum[-1] = nums[-1]
        for i in range(len(r_sum)-2, -1, -1):
            r_sum[i] = r_sum[i+1] + nums[i]
        
        for i in range(len(nums)):
            left_sum = l_sum[i-1] if i-1 >= 0 else 0
            right_sum = r_sum[i+1] if i+1 <= len(nums)-1 else 0

            if left_sum == right_sum:
                return i
        return -1
            
        


        

        