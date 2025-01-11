class Solution:
    def checkValidString(self, s: str) -> bool:
        '''

        s =  ( * ) )
                   ^

        left = []
        asterisk = [1]

        '''

        left: list[str] = []
        asterisk: list[str] = []

        for i in range(len(s)):
            if s[i] == '(':
                left.append(i)
            elif s[i] == '*':
                asterisk.append(i)
            elif s[i] == ')':
                if not left and not asterisk:
                    return False
                
                if left:
                    left.pop()
                elif asterisk:
                    asterisk.pop()

        while left and asterisk:
            left_index = left.pop()
            right_index = asterisk.pop()

            if left_index > right_index:
                return False
        
        return not left