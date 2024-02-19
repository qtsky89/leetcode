class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        '''
        str1 = 'A B A B A B' 
        str2 = 'A B A B'
                p1 p2
                A   no
                A B ok
                A B A no
                A B A B no

        try smaller length of str => str2
        '''
        
        small_str = str1 if len(str1) > len(str2) else str2
        
        # helper function    4  ABCD       2 AB
        def is_divisable(string: str, sub_str: str) -> bool:
            if len(string) % len(sub_str) != 0:
                return False
            
            factor = len(string) // len(sub_str)

            return sub_str * factor == string
            
        
        i = 0
        ret = ''
        while i <= len(small_str)-1:
            if is_divisable(str1, small_str[:i+1]) and is_divisable(str2, small_str[:i+1]):
                ret = small_str[:i+1]
            i += 1
        
        return ret
        