class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        s = a b c a b c b b
           lr


        '''

        ret = 0
        visited = set()
        l, r = 0, 0

        while r <= len(s)-1:
            while s[r] in visited:
                visited.remove(s[l])
                l += 1
            
            visited.add(s[r])

            ret = max(ret, r-l+1)

            r += 1
        
        return ret