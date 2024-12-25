class Solution:
    def calculate(self, s: str) -> int:
        '''
        s = " ( 123 + ( 4 + 5 + 2 ) - 3 ) + ( 6 + 8 ) "
                                    ^


        stack = 8, 14,
            23
        '''

        stack = []

        i = 0
        while i <= len(s)-1:
            if s[i] == " " or s[i] == "+":
                i += 1
                continue
            
            if s[i].isdigit():
                j=i
                while j <= len(s)-1 and s[j].isdigit():
                    j += 1
                
                if stack and stack[-1] == '-':
                    stack.pop()
                    stack.append(int(s[i:j]) * (-1)) # number    
                else:
                    stack.append(int(s[i:j])) # number
                
                i=j
            elif s[i] == '-':
                stack.append(s[i])
                i += 1
            elif s[i] == '(':
                stack.append(s[i])
                i += 1
            elif s[i] == ')':
                ret = 0
                while stack and stack[-1] != "(":
                    ret += stack.pop()
                stack.pop()

                if stack and stack[-1] == '-':
                    stack.pop()
                    stack.append(ret * (-1)) # number
                else:
                    stack.append(ret) # number
                i+=1

        return sum(stack)
                
                
                
            



                




