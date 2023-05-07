class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        '''
        s = a b c
            ^p1
        t = a h b g d c
            ^p2
        ret = true
        '''

        if len(s) > len(t):
            return False

        if len(s) == 0:
            return True

        p1, p2 = 0, 0
        while p1 <= len(s)-1 and p2 <= len(t)-1:
            if s[p1] == t[p2]:
                p1, p2 = p1+1, p2+1

                if p1 == len(s):
                    return True
            else:
                p2 += 1
        return False
            


        
        