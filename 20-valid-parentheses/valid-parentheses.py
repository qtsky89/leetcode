class Solution:
    def isValid(self, s: str) -> bool:
        '''
        s = () {} []

        example1.
            s = ()
            valid
        
        example2.
            s = ()[]{}
            valid

            stack = [
                    ) ] }
        
        example3.
            s = (
            not valid
        '''

        stack = []
        for i in range(len(s)):
            # start parantehses
            if s[i] in '({[':
                stack.append(s[i])
            elif s[i] == ')':
                if not stack or stack[-1] != '(':
                    return False
                stack.pop()
            elif s[i] == '}':
                if not stack or stack[-1] != '{':
                    return False
                stack.pop()
            elif s[i] == ']':
                if not stack or stack[-1] != '[':
                    return False
                stack.pop()
            
        return len(stack) == 0

                