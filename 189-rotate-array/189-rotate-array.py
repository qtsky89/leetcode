class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        tmp = nums[:]
        
        k %= len(nums)
        
        for i in range(len(nums)):
            nums[i] = tmp[i-k] if i-k >= 0 else tmp[i-k+len(tmp)]
        