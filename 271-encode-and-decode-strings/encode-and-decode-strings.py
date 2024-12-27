class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """

        '''
        encoded_str = 5*Hello5*World
        '''

        ret: list[str] = []

        for s in strs:
            ret.append(f'{len(s)}*{s}')
        
        return ''.join(ret)


    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """

        '''
        encoded_str = '5 * H e l l o 5 * W o r l d'
                      i  j     

        => ['Hello', 'World']
        
        '''

        if s == '':
            return []

        ret = []
        i = 0
        while i <= len(s)-1:
            j = i
            while j <= len(s)-1 and s[j] != '*':
                j += 1
            length = int(s[i:j])

            ret.append(s[j+1:j+1+length])

            i = (j+1+length)
        
        return ret
                



        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))