class Solution:
    def decodeString(self, s: str) -> str:
        '''

        [ ]
        1. 
        stack = [2 bc    ]
        ret = [a a a bc bc]

        2. 
        s = 3[a2[c]]

        char, [ push to stack
        ] pop out stack

        stack = [acc acc acc]
        return stack
        '''

        stack: list[str] = []

        i = 0 
        # 3 [a 2 [c]]
        while i <= len(s)-1:
            if s[i].isdigit():
                tmp = []

                while s[i].isdigit():
                    tmp.append(s[i])
                    i += 1
                stack.append(''.join(tmp))
            elif s[i] == ']':
                # c
                tmp = []
                while stack and stack[-1] != '[':
                    tmp.append(stack.pop())
                stack.pop()
                # 3
                count = stack.pop()
                stack.append(''.join(tmp[::-1] * int(count) ))
                i+=1 
            else:
                stack.append(s[i])
                i+=1
        return ''.join(stack)
                
                
