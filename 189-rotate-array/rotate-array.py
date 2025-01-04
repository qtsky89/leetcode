class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # for _ in range(k % len(nums)):
        #     item = nums.pop()
        #     nums.insert(0, item)
        
        k = k % len(nums)
        ret = [0] * len(nums)
        for i in range(len(nums)):
            ret[i] = nums[i-k]
        
        for i in range(len(nums)):
            nums[i] = ret[i]
        
 