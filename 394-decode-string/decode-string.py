class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        '''
            23[abc]
            i
              j
        '''
        i=0
        while i <= len(s)-1:
            if s[i].isdigit():
                j = i
                while j <= len(s)-1 and s[j].isdigit():
                    j += 1
                stack.append(int(s[i:j]))

                i = j
                continue
            elif s[i] == '[':
                stack.append(s[i])
                i += 1
            elif s[i].isalpha():
                stack.append(s[i])
                i += 1
            elif s[i] == ']':
                tmp = ''
                while stack and stack[-1] != '[':
                    tmp = stack.pop() + tmp
                
                '''
                tmp = abc
                '''

                # remove open bracket
                stack.pop()

                # 23, 2, 3
                times = stack.pop()
                
                stack.append(tmp * times)
                i += 1
        
        return ''.join(stack)


                
