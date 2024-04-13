class Solution:
    def minRemoveToMakeValid(self, strings: str) -> str:
        '''
        l e e t () t ( c ) o ) d e (
                                  
        open_counter = 0

        if (
            open_counter += 1
            stack.append()
        if char:
            stack.append()
        
        if )
            if open_counter > 0
                open_coutner -=1
            else:
                conintue
        
        if open_counter > 0:
            reverse order I should remove open parathesis

        '''

        open_counter =  0

        stack: list[str] = []
        for s in strings:
            if s.isalpha():
                stack.append(s)
            elif s == '(':
                open_counter += 1
                stack.append(s)
            else: # s== ')'
                if open_counter > 0:
                    open_counter -= 1
                    stack.append(s)
                else:
                    continue # skip
        
        ret = []
        for i in range(len(stack)-1, -1, -1):
            if open_counter > 0 and stack and stack[-1] == '(':
                open_counter -= 1
                stack.pop()
            else:
                ret.append(stack.pop())
        return ''.join(ret[::-1])
            