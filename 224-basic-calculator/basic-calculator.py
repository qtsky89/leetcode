class Solution:
    def calculate(self, s: str) -> int:
        '''
        s = " ( 1 + ( 4 + 5 + 2 ) - 3 ) + ( 6 + 8 )"

        stack = [8, 14]

        return sum(stack)

        '''

        i = 0
        stack: list[int|str] = []

        while i <= len(s)-1:
            if s[i] in '+ ':
                i += 1
            elif s[i] in '(-':
                stack.append(s[i])
                i += 1
            elif s[i].isdigit():
                j = i
                while j <= len(s)-1 and s[j].isdigit():
                    j += 1
                number = int(s[i:j])

                if stack and stack[-1] == '-':
                    stack.pop()
                    number = -number
                
                stack.append(number)
                i = j
            elif s[i] == ')':
                number = 0 

                while stack and stack[-1] != '(':
                    number += stack.pop()
                
                # pop out (
                stack.pop()

                if stack and stack[-1] == '-':
                    stack.pop()
                    number = -number
                
                stack.append(number)
                i += 1
        return sum(stack)
