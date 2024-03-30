class Solution:
    def decodeString(self, strings: str) -> str:
        '''
        3[a]2[bc]
        => aaabcbc

        3[a41[cdd]]
        pop trigger => ']'

        stack = 3 [ a cddcdd...]

        '''
        # stack = 3 [ a 41 
        stack: list[str | int] = []

        i = 0
        while i <= len(strings)-1:
            if strings[i].isdigit():
                tmp = ''
                while strings[i].isdigit():
                    tmp += strings[i]
                    i += 1
                stack.append(int(tmp))
                continue
            
            # do something
            if strings[i] == ']':
                tmp = ''
                while stack and stack[-1] != '[':
                    tmp = stack.pop() + tmp
                
                stack.pop() # remove '['
                stack.append(tmp * stack.pop())
            else:
                stack.append(strings[i])
            
            i += 1
        
        return ''.join(stack)
            


            