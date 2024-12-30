class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        '''
        strs = hello world

                5#hello5#hello
                       

        '''
        ret = []

        for s in strs:
            ret.append(f'{len(s)}#{s}')

        return ''.join(ret)
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        
        5 #   h  e l l o 5 # h e l l o
        i j j+1        ^       
        """

        ret = []

        i = 0
        while i <= len(s)-1:
            if s[i].isdigit():
                j = i

                while s[j] != '#':
                    j += 1
                
                length = int(s[i:j])
                
                ret.append(s[j+1:j+1+length])
                
                i = j+1+length
        
        return ret


        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))