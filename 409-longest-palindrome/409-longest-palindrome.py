from collections import Counter

class Solution:
    # s = 'abccccdd'
    def longestPalindrome(self, s: str) -> int:
        # c = {a:1, b:1, c:4, d:2}
        c = Counter(s)
        
        ret = 0
        is_odd_count = False
        for key in c:
            if c[key] %2 == 0:
                ret += c[key]
            elif c[key] > 2:
                ret += c[key]-1
                is_odd_count = True
            else:
                is_odd_count = True
        
        if is_odd_count:
            ret += 1
        
        return ret