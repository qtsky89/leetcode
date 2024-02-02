class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        '''
        s = 'abc', t = 'ahbgdc'

        len(s) <= len(t)
        '''

        p1, p2 = 0, 0

        while p1 <= len(s)-1 and p2 <= len(t) - 1:
            if s[p1] == t[p2]:
                p1 += 1
                p2 += 1
            else:
                p2 += 1

        return p1 == len(s)