class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """

        '''
        strs = ['a', 'b', 'c']
        
        3#abc

        '''

        ret = []

        for s in strs:
            ret.append(f'{len(s)}#{"".join(s)}')
        return ''.join(ret)
        
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """

        '''
        3#abc
        '''

        ret = []
        i=0
        while i<=len(s)-1:
            j = i
            while s[j].isdigit():
                j += 1
            length = int(s[i:j])
            ret.append(s[j+1:j+1+length])
            i = j+1+length
        
        return ret
        
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))