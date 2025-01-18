class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        '''
        nums=  2, 3, 1, 2, 4, 3   target = 7
              l         r                  current_sum=8    ret = 3

        '''

        l, r = 0, 0

        min_length = float('inf')
        current_sum = 0
        while r <= len(nums)-1:
            current_sum += nums[r]

            while l <= r and current_sum >= target:
                if current_sum >= target:
                    min_length = min(min_length, r-l+1)

                current_sum -= nums[l]
                l += 1
            r += 1
        return min_length if min_length != float('inf') else 0

            