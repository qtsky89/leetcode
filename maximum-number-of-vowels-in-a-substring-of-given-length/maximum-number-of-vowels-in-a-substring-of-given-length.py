class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        '''
        s =                a b c i i i d e f
        accumulate_count = 0 0 0 1 2 3 3 3 3
                           ^0    ^3
                           k = 3
        '''
        accumulate_count = [0] * len(s)
        for i in range(len(accumulate_count)):
            tmp = 1  if s[i] in 'aeiou' else 0

            if i == 0:
                accumulate_count[i] = tmp
            else:
                accumulate_count[i] = accumulate_count[i-1] + tmp

        max_diff = accumulate_count[k-1]
        for i in range(k, len(accumulate_count)):
            max_diff = max(max_diff, accumulate_count[i] - accumulate_count[i-k])
        return max_diff





