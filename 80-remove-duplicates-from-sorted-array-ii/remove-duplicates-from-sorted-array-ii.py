class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        w, r = 0, 0

        count = defaultdict(int)
        while r <= len(nums)-1:
            if count[nums[r]] <= 1:
                nums[w] = nums[r]
                w += 1
            count[nums[r]] += 1
            r += 1
        return w