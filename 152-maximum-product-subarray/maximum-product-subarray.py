class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        nums = [2, 3, -2, 4]

        keep the maximum
        keep the minimum

        0 
        maximum => 1
        minimum -> 1
        '''

        max_value = max(nums)

        cur_max, cur_min = 1, 1

        for i in range(len(nums)):
            if nums[i] == 0:
                cur_max, cur_min = 1, 1
                continue

            cur_max, cur_min = max(nums[i], cur_max * nums[i], cur_min * nums[i]), min(nums[i], cur_max * nums[i], cur_min * nums[i])
            

            max_value = max(max_value, cur_max)
        
        return max_value
