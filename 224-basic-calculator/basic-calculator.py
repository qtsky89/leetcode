class Solution:
    def calculate(self, s: str) -> int:
        stack = []

        i = 0

        while i <= len(s) -1 :
            if s[i] == ' ' or s[i] == '+':
                i+=1
                continue
            
            if s[i] == '(':
                stack.append(s[i])
                i+=1
            elif s[i].isdigit():
                j = i+1

                while j <= len(s)-1 and s[j].isdigit():
                    j+=1
                
                tmp = int(s[i:j])
                if stack and stack[-1] == '-':
                    stack.pop()
                    tmp *= -1
                stack.append(tmp)

                i = j
            elif s[i] == '-':
                stack.append(s[i])
                i+=1
            elif s[i] == ')':
                ret = 0

                while stack and stack[-1] != '(':
                    ret += stack.pop()
                stack.pop()

                if stack and stack[-1] == '-':
                    stack.pop()
                    ret *= -1
                
                stack.append(ret)
                i += 1
        return sum(stack)







