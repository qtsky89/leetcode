class Solution:
    def reverseVowels(self, s: str) -> str:
        '''
        s =   [l e e t c o d e]
                 p1          p2
        '''

        p1, p2 = 0, len(s)-1
        ret = list(s)

        while p1 < p2:
            if s[p1] not in 'aeiouAEIOU':
                p1 += 1
            elif s[p2] not in 'aeiouAEIOU':
                p2 -= 1
            else:
                ret[p1], ret[p2] = ret[p2], ret[p1]
                p1, p2 = p1+1, p2-1
        
        return ''.join(ret)


        

