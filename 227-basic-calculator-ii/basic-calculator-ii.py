class Solution:
    def calculate(self, s: str) -> int:
        '''
        s = 3 - 3 * 2 = -3

        stack  = 3 -3 * 2
        '''
        
        i = 0
        stack = []

        while i < len(s):
            if s[i].isdigit():
                j = i
                while j < len(s) and s[j].isdigit():
                    j += 1
                number = int(s[i:j])

                if stack and stack[-1] == '*':
                    stack.pop() # remove *
                    operand = stack.pop()
                    number *= operand
                elif stack and stack[-1] == '/':
                    stack.pop() # remove /
                    operand = stack.pop()
                    number = int(operand / number)

                if stack and stack[-1] == '-':
                    stack.pop() # remove minus operator
                    number = -number

                stack.append(number)
                i = j
            elif s[i] == '+' or s[i] == ' ': # ignore
                i += 1
            elif s[i] in '-*/':
                stack.append(s[i])
                i += 1
            

        return sum(stack)