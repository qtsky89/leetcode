class Solution:
    def removeStars(self, s: str) -> str:
        '''
        s = "l e e t * * c o d * e"

        stack = [l e c o e]
        ''.join
        '''

        stack = []

        for i in range(len(s)):
            if s[i] == '*':
                stack.pop()
            else:
                stack.append(s[i])
        
        return ''.join(stack)