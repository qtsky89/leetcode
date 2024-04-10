class Solution:
    def romanToInt(self, s: str) -> int:
        '''
        s = MCMXCIV
        '''

        dic = {
            'I': 1,
            'V': 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

        ret = 0
        i = 0
        while i <= len(s)-1:
            if ((s[i] == 'I' and i+1 <= len(s) -1 and s[i+1] in 'VX') or
                (s[i] == 'X' and i+1 <= len(s) -1 and s[i+1] in 'LC') or
                (s[i] == 'C' and i+1 <= len(s) -1 and s[i+1] in 'DM')):
                ret -= dic[s[i]]
            else:
                ret += dic[s[i]]
            i += 1
                
        return ret
        