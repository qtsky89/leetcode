class Solution:
    def calculate(self, s: str) -> int:
        '''
        s = 3 - 5 * 2 / 3
                        ^
        stack = 3, -3


        return sum(stack)
        '''

        i = 0
        stack: list[int|str] = []

        while i <= len(s)-1:
            if s[i].isdigit():
                j = i

                while j <= len(s)-1 and s[j].isdigit():
                    j += 1
                number = int(s[i:j])

                if stack and stack[-1] == '*':
                    stack.pop()
                    operand = stack.pop()
                    number *= operand
                elif stack and stack[-1] == '/':
                    stack.pop()
                    operand = stack.pop()
                    number = int(operand / number)

                if stack and stack[-1] =='-':
                    stack.pop()
                    number = -number
                
                stack.append(number)

                i = j
            elif s[i] in '+ ':
                i += 1
            elif s[i] in '*/-':
                stack.append(s[i])
                i += 1

        return sum(stack)

