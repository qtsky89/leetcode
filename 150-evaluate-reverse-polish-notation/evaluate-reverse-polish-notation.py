class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        operations = + - * /

        token = [2, 1, +, 3, *]

        
        '''

        stack = []

        for token in tokens:
            if token not in '+-*/':
                stack.append(int(token))
                continue
            
            match token:
                case '+':
                    o2 = stack.pop()
                    o1 = stack.pop()

                    stack.append(o1 + o2)
                case '-':
                    o2 = stack.pop()
                    o1 = stack.pop()

                    stack.append(o1-o2)
                case '*':
                    o2 = stack.pop()
                    o1 = stack.pop()

                    stack.append(o1*o2)
                case '/':
                    o2 = stack.pop()
                    o1 = stack.pop()

                    stack.append(int(o1 / o2))
        return stack[0]
            
                
