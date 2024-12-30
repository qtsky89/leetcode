class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        '''
        count = {
            

        }
        s =    a, b  k = 1
              ^^
        '''

        if k == 0:
            return 0

        ret = 0
        p1, p2 = 0, 0
        count = defaultdict(int)

        while p2 <= len(s) -1:
            count[s[p2]] += 1

            while len(count) > k:
                count[s[p1]] -= 1
                if count[s[p1]] == 0:
                    del count[s[p1]]
                p1 += 1
            ret = max(ret, p2-p1+1)

            p2 += 1
        
        return ret
            