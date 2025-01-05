class Solution:
    def decodeString(self, s: str) -> str:
        '''
        3 [ a 2 [ c ] ]
                  ^

        stack = 3 [ a 2
        '''

        stack = []
        i = 0
        while i<=len(s)-1:
            if s[i].isdigit():
                j = i

                while s[j].isdigit():
                    j += 1
                
                stack.append(int(s[i:j]))
                i = j
            elif s[i] == '[':
                stack.append(s[i])
                i += 1
            elif s[i].isalpha():
                stack.append(s[i])
                i += 1
            elif s[i] == ']': # pop the all value including open braket
                tmp = ''
                while stack and stack[-1] != '[':
                    tmp = stack.pop() + tmp
                
                # remove open bracket. not using that
                stack.pop()

                # count
                count = stack.pop()
                stack.append(tmp * count)
                i += 1
        
        return ''.join(stack)
