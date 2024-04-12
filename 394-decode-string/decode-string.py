class Solution:
    def decodeString(self, s: str) -> str:
        '''
        k[encoded_string]

        example1.
            s = 3[a]2[bc]
            ret = aaabcbc
        
        example2.
            s = 13 [ a 2 [ c ] ]
                               ^
            
            stack = accaccacc...
                'acc' * 13
        example3.
            s = 2[abc]3[cd]ef
            ret = abcabccdcdcdef
        '''

        stack = []

        i = 0
        while i <= len(s)-1:
            # handle digit
            if s[i].isdigit():
                tmp = ''
                while s[i] != '[':
                    tmp += s[i]
                    i += 1
                stack.append(int(tmp))
                continue
            
            if s[i] == ']':
                tmp = ''
                
                while stack and stack[-1] != '[':
                    tmp = stack.pop() + tmp
                
                stack.pop() # remove [

                tmp = tmp * stack.pop() # get number
                stack.append(tmp)
            else:
                stack.append(s[i])
            
            i+=1
        return ''.join(stack)
            
                



