class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        '''
        s =  e c e b a
            lr

        count_map = {
            a : 1
            b : 1
        }
        k=2
        '''

        if k == 0:
            return 0

        count_map: defaultdict[str, int] = defaultdict(int)

        longest_length = 0
        l, r = 0, 0

        while r <= len(s)-1:
            count_map[s[r]] += 1

            while l <= r and len(count_map) > k:
                count_map[s[l]] -= 1

                if count_map[s[l]] == 0:
                    del count_map[s[l]]

                l += 1

            longest_length = max(longest_length, r-l+1)
            
            r += 1

        return longest_length

        
        