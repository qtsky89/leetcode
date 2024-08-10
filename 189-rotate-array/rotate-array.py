class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        
        new_nums = [*nums[-k:], *nums[:-k]]

        for i in range(len(nums)):
            nums[i] = new_nums[i]
