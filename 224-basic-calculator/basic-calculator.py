class Solution:
    def calculate(self, s: str) -> int:
        '''
        s = ( 1 + ( 4 + 5 + 2 ) - 3 ) + ( 6 + 8 )
                              ^
        stack = 8 14
        '''

        i = 0
        stack = []
        while i < len(s):
            if s[i] == '(':
                stack.append(s[i])
                i += 1
            elif s[i].isdigit():
                j = i
                while j < len(s) and s[j].isdigit():
                    j += 1
                number = int(s[i:j])

                if stack and stack[-1] == '-':
                    stack.pop()
                    number = -number

                stack.append(number)
                i = j
            elif s[i] == '+' or s[i] == ' ': # ignore
                i += 1
            elif s[i] == '-':
                stack.append(s[i])
                i += 1
            elif s[i] == ')': # pop out stacks
                number = 0
                
                while stack and stack[-1] != '(':
                    number += stack.pop()
                
                stack.pop() # remove open parenthesis (
                
                if stack and stack[-1] == '-':
                    stack.pop()
                    number = -number
                stack.append(number)    
                i += 1

        print(stack)

        return sum(stack)