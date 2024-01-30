class Solution:
    def decodeString(self, s: str) -> str:
        '''
        k[encoded_string]


        2[abc]3[cd]ef
        '''
        stack = []
        i = 0
        while i <= len(s)-1:            
            if s[i].isdigit():
                tmp = []
                while s[i].isdigit():
                    tmp.append(s[i])
                    i+=1
                stack.append(int(''.join(tmp)))
                continue
            elif stack and s[i] in 'abcdefghijklmnopqrstuvwxyz[':
                stack.append(s[i])
            elif stack and s[i] == ']':
                tmp = []
                while stack and stack[-1] != '[':
                    tmp.insert(0, stack.pop())
                stack.pop()
                stack.append(''.join(tmp * int(stack.pop()) ))
            else:
                stack.append(s[i])
            i+=1
        return ''.join(stack)

