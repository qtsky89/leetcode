class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        '''
        nums = [1,2,3,4] k=5


        nums = [1, 3, 3, 3, 4]
                   ^     ^     k=6
        '''

        nums.sort()
        p1, p2 = 0, len(nums)-1

        op_count = 0
        while p1 < p2:
            if nums[p1] + nums[p2] == k:
                p1 += 1
                p2 -= 1
                op_count += 1
            elif nums[p1] + nums[p2] > k:
                p2 -= 1
            else:
                p1 += 1
        return op_count