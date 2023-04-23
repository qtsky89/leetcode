import re

class Solution:
    def reverseWords(self, s: str) -> str:
        '''
        s   = 'the sky is blue'
        ret = 'blue is sky the'
        '''

        s = s.strip()
        s_list = re.split('\s+', s)
        s_list = s_list[::-1]

        return ' '.join(s_list)

        
