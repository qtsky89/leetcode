class Solution:
    def sum(self, prefix_nums: list[int], i: int, j: int) -> int:
        return prefix_nums[j] - (prefix_nums[i-1] if i-1 >= 0 else 0)
        

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        '''
        nums =  2  3  1  2  4  3    target = 7
                   ^     ^
                
             =>  2, 5, 6, 8, 12, 15
        '''

        ret = float('inf')

        prefix_sum = [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]

        i, j = 0, 0
        while j <= len(nums)-1:
            while i <= j and self.sum(prefix_sum, i, j) >= target:
                ret = min(ret, j-i+1)
                i += 1

            j += 1
        
        return ret if ret != float('inf') else 0