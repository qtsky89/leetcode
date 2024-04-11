class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        nums = 100 4 200 1 3 2

        '''

        visited = set(nums)

        max_lengh = 0
        count = 0 
        for i in range(len(nums)):
            if nums[i]-1 in visited:
                continue
            
            tmp = nums[i]
            count = 0
            while tmp in visited:
                tmp += 1
                count += 1
            
            max_lengh = max(max_lengh, count)
        return max_lengh
                
            