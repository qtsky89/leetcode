class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        s =  A   A   B   A   B   B   A                valid : (p2-p1+1) - most_count >= k 
            ^^                            0-0+1 - 1 >= k    valid=True, res = 1
            ^    ^                        1-0+1 - 2 >= k    valid = True res = 2
        '''

        p1, p2 = 0, 0

        counter = [0] * 26
        counter[ord(s[p1]) - ord('A')] += 1
        max_ret = 0
        while p2 <= len(s)-1:
            # check valid
            most_count = max(counter)
            if (p2-p1+1 - most_count) > k:
                counter[ord(s[p1]) - ord('A')] -= 1
                p1 += 1
            else:
                max_ret = max(max_ret, p2-p1+1)
                p2 += 1
                if p2 <= len(s)-1:
                    counter[ord(s[p2]) - ord('A')] += 1
        return max_ret
            