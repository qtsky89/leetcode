class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        '''
        s = 'a b c'  t = 'a h b g d c'
             ^            ^
               ^            ^
               ^              ^
                   ^                  ^
        
        s = 'a x c'  t = 'a h b g d c'
                          ^         ^ False
        '''

        if not s:
            return True

        p1, p2 = 0, 0

        while p1 <= len(s)-1 and p2 <= len(t) -1:
            if s[p1] == t[p2]:
                p1 += 1
            p2 += 1
        
        return p1 == len(s)