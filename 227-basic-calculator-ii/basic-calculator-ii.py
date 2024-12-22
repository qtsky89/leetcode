class Solution:
    def calculate(self, s: str) -> int:
        i = 0

        stack = []

        is_minus = False
        while i <= len(s)-1:
            if s[i] == " " or s[i] == '+':
                i+=1
            elif s[i].isdigit():
                tmp = ''
                j = i
                while j <= len(s)-1 and s[j].isdigit():
                    j += 1
                
                if is_minus:
                    tmp = '-' + s[i:j]
                    is_minus = False
                else:
                    tmp = s[i:j]
                i = j

                if stack and stack[-1] == '*':
                    stack.pop()
                    stack.append(int(stack.pop()) * int(tmp))
                elif stack and stack[-1] == '/':
                    stack.pop()
                    stack.append(int(int(stack.pop()) / int(tmp)))
                else:
                    stack.append(int(tmp))
            elif s[i] == '-':
                is_minus = True
                i += 1
            elif s[i] in '*/':
                stack.append(s[i])
                i += 1

        return sum(stack)