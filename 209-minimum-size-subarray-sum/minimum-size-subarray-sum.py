class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        '''
        nums =  2 3 1 2 4 3
                ^ ^
        target = 7

        tmp = 2

        minimum_length = 4 -> 3 -> 2
        '''

        p1, p2 = 0, 0
        minimum_length = float('inf')
        tmp = nums[0]

        while p1 <= p2 and p2 <= len(nums)-1:
            if tmp >= target:
                minimum_length = min(minimum_length, p2-p1+1)
                tmp -= nums[p1]
                p1 += 1
            else:
                p2 += 1
                if p2 <= len(nums)-1:
                    tmp += nums[p2]

        return minimum_length if minimum_length != float('inf') else 0