class Solution:
    def reverseVowels(self, string: str) -> str:
        '''
        s = ' h e l l o A d'
                ^       ^
        '''

        s = list(string)

        p1, p2 = 0, len(s)-1

        while p1 < p2:
            while p1 <= len(s)-1 and s[p1] not in 'aeiouAEIOU':
                p1 += 1
            
            while p2 >= 0 and s[p2] not in 'aeiouAEIOU':
                p2 -= 1
            
            if p1 < p2:
                s[p1], s[p2] = s[p2], s[p1]

            p1, p2 = p1+1, p2-1
        
        return ''.join(s)
            