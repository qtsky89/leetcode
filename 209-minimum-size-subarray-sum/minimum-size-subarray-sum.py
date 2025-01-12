class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        '''
        taret = 7, nums = 2, 3, 1, 2, 4, 3
                          ^^                       2            min_val = float('inf')
                          ^  ^                     5            min_val = float('inf')
                          ^     ^                  6            min_val = float('inf')
                          ^        ^               8            min_val = 4
                              ^    ^               6            min_val = 4
                              ^        ^           10           min_val = 4
                                 ^     ^           7            min_val = 3
                                    ^  ^           6            min_val = 3
                                    ^     ^        9            min_val = 3
                                       ^  ^        7            min_val = 2
                                          ^^       3            min_val = 2
        '''

        min_length = float('inf')
        l, r = 0, 0

        cur_sum = 0
        while r < len(nums):
            cur_sum += nums[r]

            while l <= r and cur_sum >= target:
                min_length = min(min_length, r-l+1)
                cur_sum -= nums[l]
                l += 1

            r += 1
        return min_length if min_length != float('inf') else 0

