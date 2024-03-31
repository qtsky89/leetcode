class Solution:
    def isValid(self, strings: str) -> bool:
        '''
        stack = "({(  "

        '''

        stack: list[str] = []

        for s in strings:
            if s in '({[':
                stack.append(s)
                continue
            
            if s in ')}]':
                if s == ')' and (not stack or stack[-1] != '('):
                    return False
                
                if s == '}' and (not stack or stack[-1] != '{'):
                    return False
                
                if s == ']' and (not stack or stack[-1] != '['):
                    return False

                stack.pop()
        return len(stack) == 0