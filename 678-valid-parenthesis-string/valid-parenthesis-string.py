class Solution:
    def checkValidString(self, s: str) -> bool:
        '''
        s = ( * ) )
                ^

            ) * <= edgecase to deal with

        open_stack = [ 0 ]

        asterisk_stack = [ 1 ]
        '''

        open_stack = []
        asterisk_stack = []

        for i in range(len(s)):
            if s[i] == '(':
                open_stack.append(i)
            elif s[i] == '*':
                asterisk_stack.append(i)
            elif s[i] == ')':
                if open_stack:
                    open_stack.pop()
                elif asterisk_stack:
                    asterisk_stack.pop()
                else:
                    return False
        
        while open_stack and asterisk_stack:
            i = open_stack.pop()
            j = asterisk_stack.pop()

            if j < i:
                return False
        
        return not open_stack