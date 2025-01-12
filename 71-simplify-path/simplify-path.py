class Solution:
    def simplifyPath(self, path: str) -> str:
        '''
        path = /home/user/Documents/../Pictures

        tmp = '', home, user, Documents, .., Pictures
                                         ^
        stack = home, user, Documents
        '''

        tmp = path.split('/')

        stack = []

        for t in tmp:
            if t == '' or t == '.':
                continue
            
            if t == '..' and stack:
                stack.pop()
            elif t == '..':
                continue
            else:
                stack.append(t)

        return '/' + '/'.join(stack)

            
        