class Solution:
    def checkValidString(self, s: str) -> bool:
        '''
        Input: s = " ( * ) ) "
                             ^

        Output: true

        left_stack = 
        asterisk_stack =  
        '''

        left_stack = []
        asterisk_stack = []

        for i in range(len(s)):
            if s[i] == '(':
                left_stack.append(i)
            elif s[i] == '*':
                asterisk_stack.append(i)
            elif s[i] == ')':
                if (not left_stack) and (not asterisk_stack):
                    return False
                elif left_stack:
                    left_stack.pop()
                elif asterisk_stack:
                    asterisk_stack.pop()

        while left_stack and asterisk_stack:
            tmp_left = left_stack.pop()
            tmp_asterisk = asterisk_stack.pop()

            # * (
            if tmp_asterisk < tmp_left:
                return False

        return not left_stack
