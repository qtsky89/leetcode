class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        '''
        str1 = 'ABCABC'
        str2 = 'ABC'
        ret = 'ABC'

        output's length coulnd't be more than short argument.
        len(ret) < len(ret2)
        '''

        large, small = '',''
        if len(str1) > len(str2):
            large, small = str1, str2
        else:
            large, small = str2, str1

        i = len(small)-1
        ret = ''
        while i >= 0:
            if self.is_dividable(large, small[:i+1]) and self.is_dividable(small, small[:i+1]):
                return small[:i+1]
            i -= 1
        return ret
   
    # hay="hello" needle="he"
    def is_dividable(self, hay: str, needle: str) -> bool:
        if len(hay) % len(needle) != 0:
            return False

        return list(hay) == (list(needle) * (len(hay) // len(needle)))
            

        

        