class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # c = {0:2, 1:1, 3:1, 12:1}
        c = Counter(nums)
        
        zero_count = c[0]
        while c[0]:
            nums.remove(0)
            c[0] -= 1
        
        #nums = [1,3,12]
        nums += [0] * zero_count
        