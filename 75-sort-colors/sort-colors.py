class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        c = defaultdict(int)
        '''
        c = {
            0 : 0
            1 : 0
            2 : 0
        }
        '''

        for num in nums:
            c[num] += 1

        i = 0
        for _ in range(c[0]):
            nums[i] = 0
            i += 1
        
        for _ in range(c[1]):
            nums[i] = 1
            i += 1

        for _ in range(c[2]):
            nums[i] = 2
            i += 1
        
            
        