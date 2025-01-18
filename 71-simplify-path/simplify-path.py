class Solution:
    def simplifyPath(self, path: str) -> str:
        '''
        /home/user/Documents/../Pictures

        tmp = ['', 'home', 'user', 'Documents', '..', 'Pictures']
        '''

        tmp = path.split('/')

        stack = []

        for t in tmp:
            if t == '' or t == '.':
                continue

            if t == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(t)
        
        return '/' + '/'.join(stack)
        