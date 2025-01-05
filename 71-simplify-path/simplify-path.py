class Solution:
    def simplifyPath(self, path: str) -> str:
        ret = path.split('/')

        if len(ret) == 1:
            return '/'
        
        stack = []
        i = 0
        while i <= len(ret)-1:
            if ret[i] == "" or ret[i] == ".":
                i+=1
                continue
            if ret[i] == "..":
                i += 1
                if stack:
                    stack.pop()
                continue

            stack.append(ret[i])
            i += 1
        
        
        return '/' + '/'.join(stack)