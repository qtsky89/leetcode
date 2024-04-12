class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        '''
        haystack = s a d b u t s a d
                   ^   ^
                     ^   ^
                       ^   ^
                         ^   ^
        needle = b u t
        '''

        p1, p2 = 0, len(needle)-1

        while p2 <= len(haystack)-1:
            if haystack[p1:p2+1] == needle:
                return p1
            p1, p2 = p1+1, p2+1
        
        return -1